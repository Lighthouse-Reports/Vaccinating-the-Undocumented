# Codebook for Tables in /output

## `main_data.csv`

- `Country`: Country name
- `Policy Transparency`: Weighted score for Policy Transparency indicator
- `Undocumented Access`: Weighted score for Undocumented Access indicator
- `Identification and Residency Requirements`: Weighted score for Identification and Residency Requirements indicator
- `Marginalized Access`: Weighted score for Marginalized Access indicator
- `Privacy Guarantees`: Weighted score for Privacy Guarantees indicator
- `Total Score`: Total weighted score
- Individual question points (T1, A2, etc.): Unweighted scores for each question converted to points by using the point system in `/data/response_score_matrix.csv`

## `confidence_scores_by_country.csv`

- `Country`: Country name
- `Confidence`: A score on the scale of 0.0 and 1.0 showing the confidence on the results of each country.