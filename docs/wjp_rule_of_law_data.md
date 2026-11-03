# WJP Rule of Law Dataset

## 1. Purpose
This dataset provides a more detailed examination of Rule of Law across selected ASEAN countries. It supplements the broad WGI measure with indicators covering civil justice, criminal justice, judicial checks, and public security.

## 2. Data Source
- Source: World Justice Project (WJP) — Rule of Law Index.
- Dataset: Historical Data workbook, manually downloaded from the WJP website.
- Historical period selected: 2012–2024.
- Original workbook contains historical editions extending beyond the selected research period.

## 3. Selected Indicators
A total of 19 indicators were selected for Level 1A.1 — Rule of Law.

**Civil Justice — Factor 7**
- 7.1 Access to and affordability of civil justice.
- 7.2 Civil justice free of discrimination.
- 7.3 Civil justice free of corruption.
- 7.4 Civil justice free of improper government influence.
- 7.5 Civil justice not subject to unreasonable delay.
- 7.6 Civil justice effectively enforced.
- 7.7 Accessible, impartial, and effective alternative dispute resolution.

**Criminal Justice — Factor 8**
- 8.1 Effective criminal investigation.
- 8.2 Timely and effective criminal adjudication.
- 8.3 Effective correctional system in reducing criminal behaviour.
- 8.4 Impartial criminal justice system.
- 8.5 Criminal justice system free of corruption.
- 8.6 Criminal justice system free of improper government influence.
- 8.7 Due process and rights of the accused.

**Judicial Checks and Public Security — Supplementary**
- 1.2 Government powers effectively limited by the judiciary.
- 5.1 Crime effectively controlled.
- 5.2 Civil conflict effectively limited.

## 4. Geographical and Historical Coverage
- Countries: 8 ASEAN countries (Brunei, Laos, and Timor-Leste are absent).
- Reporting periods: 11, from 2012–2013 through 2024.
- Total country-period records: 87.
- Myanmar's first available period: 2014.
- Available selected indicator observations: 1,653 out of 1,653 possible except for two missing values in indicator 8.3.
- Missing observations: 2 (Indonesia and Myanmar, both for indicator 8.3).

## 5. Processing and Validation
The original Excel workbook was processed using Python and pandas.
- Selected indicators were extracted from the consolidated historical worksheet.
- Duplicate country-period records: 0.
- Historical score validation: 1,843 comparisons against the original 2012–2013 worksheet.
- Matching scores: 1,843.
- Mismatching scores: 0.
- Missing values were retained rather than replaced with zero.

## 6. Methodological Considerations
WJP combines General Population Polls, Qualified Respondents' Questionnaires, and selected third-party data. Scores generally range from 0 to 1.

The historical dataset contains changes in factor numbering, terminology, and methodology. In particular, the 2012–2013 edition used different numbering for Order and Security and some other indicators. The consolidated dataset preserves the numerical scores, but matching scores do not prove that definitions and methodologies remained unchanged.

The WJP series should therefore be interpreted cautiously over time. It is supplementary to WGI, not a fully independent confirmation, because WJP is among WGI's underlying information sources.

The three selected indicator groups should be analysed separately. Parent factor scores and their subfactor scores should not be combined indiscriminately, as this can result in double counting.

## 7. Output
`data/processed/asean_wjp_rule_of_law_2012_2024.csv`

The dataset supports detailed regional comparisons of judicial institutions and public security. It does not, by itself, establish causal relationships.