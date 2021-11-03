# Codebook for Tables in /output

## `main_data.csv`

- `Country`: Country name; Country list:
    - Bulgaria, Czech Republic, Denmark, Estonia, France, Germany, Austria, Greece, Cyprus, Ireland, Italy, Luxembourg, Netherlands, Poland, Portugal, Romania, Slovakia, Spain, United Kingdom, Malta
- `Policy Transparency`: Weighted score for Policy Transparency category/indicator
- `Undocumented Access`: Weighted score for Undocumented Access category/indicator
- `Identification and Residency Requirements`: Weighted score for Identification and Residency Requirements category/indicator
- `Marginalized Access`: Weighted score for Marginalized Access category/indicator
- `Privacy Guarantees`: Weighted score for Privacy Guarantees category/indicator
- `Total Score`: Total weighted score
- Individual question points (`T1, A2`, etc.): Unweighted scores for each question converted to points by using the point system in `/data/response_score_matrix.csv`

## `confidence_scores_by_country.csv`

- `Country`: Country name (see above for country list)
- `Confidence`: A score on the scale of 0.0 and 1.0 showing the confidence on the results of each country.