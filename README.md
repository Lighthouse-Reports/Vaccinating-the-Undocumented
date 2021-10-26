# Vaccinating the Undocumented

## Data

### /output

- `main_data.csv` holds all preprocessed data including:
  - Question level values (`T1`, `A1`, etc.)
  - Category level aggregations (`Policy Transparency`, `Undocumented Access`, etc.) and
  - `Total score`

- `confidence_scores_by_country.csv` holds confidence scores by country:
  - Confidence score falls in \[0.0,1.0\]
  - The higher the score, the higher the confidence

### /data

- All raw data and question meta data such as question importances are located in this folder.
- See code book inside /data folder for details.

## How to Run the Notebooks

1. Clone the repository
2. (Optional) Create a python environment and activate
3. Install required modules in `requirements.txt`
4. Start jupyterlab
5. You may run `notebooks/data-preprocessing.ipynb`. However, the output folder already contains the data processed in this notebook.
6. For consistency results, open and run `notebooks/internal-consistency-checks.ipynb`
