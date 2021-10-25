import pandas as pd
import numpy as np


def point_extract(item):
    # This extract the point scores from the dataframe
    item = str(item)
    point = np.nan if item.startswith('--') else item.split('|')[0]
    return float(point)


def get_point_matrix():
    qc = pd.read_csv('../data/response_score_matrix.csv')
    qc['Original Question Number'] = [i.replace('"', '').replace('Rewritten', '').strip() for i in qc['Original Question Number']]
    qc.set_index('Original Question Number', inplace = True)
    qc = qc.T

    qc['Yes'] = qc.Yes.apply(point_extract)
    qc['No'] = qc.No.apply(point_extract)
    qc['Unknown'] = qc.Unknown.apply(point_extract)
    qc['NA'] = qc.NA.apply(point_extract)
    return qc


def convert2points(question_number, response_series, point_matrix):
    return [point_matrix.loc[question_number, response] for response in response_series]


def get_category(point_matrix):
    category = pd.Series(point_matrix.Category)
    category.index = point_matrix.index
    return category


def get_question_importances():
    STEP = 0.5
    MID = 1.0
    ordinal2number = {
        'not so important': MID  - STEP,
        'important': MID,
        'very important': MID + STEP
    }
    tmp = pd.read_csv('../data/questions_cleaned.csv')
    qi = tmp.iloc[8, 1:]
    qi = qi.apply(lambda x: x.strip().lower())
    question_importance = pd.Series([ordinal2number[v] for v in qi])
    question_importance.index = qi.index
    return question_importance


def load_responses():
    # Row 0 and 1 are question text and category. So drop them.
    raw = pd.read_csv('../data/final_responses.csv').iloc[2:, :]

    raw.rename(columns = {'Original Question Number': 'Country'}, inplace = True)
    raw.set_index('Country', inplace = True)

    # We want to select every 5th column starting at 0 to only keep the responses
    n_items_per_question = 5
    raw = raw.loc[:, [(k % n_items_per_question) == 0 for k in range(raw.shape[1])]]

    # Replace nan by "NA"
    raw.fillna('NA', inplace = True)
    return raw


def get_results(raw, point_matrix):
    res = raw.copy(deep = True)
    if not isinstance(raw.iloc[0, 0], float):
        for c in raw.columns:
            res[c] = convert2points(c, res[c], point_matrix)
    return res


def get_keywords():
    kw = pd.read_csv('../data/questions_extra_props.csv')
    keyword = kw.Keyword
    keyword.index = kw.Item
    return keyword

# -------------------------------------------------------------------------------------

point_matrix = get_point_matrix()
category = get_category(point_matrix)
question_importance = get_question_importances()
raw = load_responses()
res = get_results(raw, point_matrix)
keyword = get_keywords()
