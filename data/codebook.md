# Codebook for Files in `/data`

## `final_responses.csv`

- First row contains the question number as a code `T1, T2, A1` etc. where T and A refers to transparency or accessibility question. NOTE: A18 is considered as a transparency question.
- Each question has 5 components:
    - Question text
    - Code of the document referenced: the code given to the documents being referenced. The document details can be found in `data\list_of_documents_used_for_national_scorecards.csv`
    - Excerpt of relevant text: Excerpt that allowed researcher to reach the conclusion to this question
    - Translation of text excerpt in English: Translation if not in English
    - Comments: Additional comments from the researcher

## `list_of_documents_used_for_national_scorecards.csv`

- Code: Unique code for each document with country identifier
- Country
- Title Of Document Or Source
- English Translation Of Title (When Applicable)
- Source Type
- Type Of Document Or Source
- Link To Document Or Source
- Date Of Publication
- Language
- Date Entered: Date recorded in this file
- Brief Explanation And Notes

## `questions_cleaned.csv`

- Question importances are coded in this file at the bottom row
- The meaning of each response to the question is explained

## `questions_extra_props.csv`

This contains the extra properties of each question.

- Keyword: Used for internal consistency tests
- The rest are not currently in use

## `response_score_matrix.csv`

- This defines the point system for each response to each question.
- It ranges from -2.0 to +1, depending on the how good or bad of an impact such a response has in vaccinating the undocumented population
