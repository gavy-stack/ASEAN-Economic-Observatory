# WGI Rule of Law Dataset Documentation

**Project:** ASEAN Economic Observatory  
**Framework classification:** Level 1A — Institutional Quality  
**Subdimension:** 1A.1 — Rule of Law  
**Data source:** World Bank — Worldwide Governance Indicators (WGI)  
**World Bank API Source ID:** 3 (revised WGI series)  
**Research period:** 1996–2024  
**Geographical coverage:** 11 ASEAN member countries  
**Output file:** `data/processed/asean_wgi_rule_of_law_1996_2024.csv`

---

## 1. Purpose

This dataset measures the Rule of Law dimension of institutional quality across ASEAN countries.

It provides a broad comparative measure of institutional performance, particularly regarding confidence in and adherence to the rules of society, contract enforcement, property rights, policing, judicial institutions, crime, and violence.

Within the ASEAN Economic Observatory framework, WGI Rule of Law serves as a core indicator of institutional quality under Level 1A.1.

The dataset is intended to support historical comparisons across ASEAN countries and subsequent analysis of the relationship between institutional quality, government capacity, public investment, financial development, and economic and social outcomes.

## 2. Data Source

The dataset was obtained from the World Bank's Worldwide Governance Indicators (WGI) through the World Bank API.

**Selected API source:** Source ID 3 — Worldwide Governance Indicators (revised series).

The revised series was selected to maintain consistency with the updated WGI methodology and its recalculated historical estimates.

Earlier observations retrieved using Source ID 2 were excluded from the final dataset.

**API endpoint structure:**

`https://api.worldbank.org/v2/country/{country_code}/indicator/{indicator_code}`

API parameters:

- `date=1996:2024`
- `format=json`
- `per_page=100`
- `source=3`

The revised WGI metadata retrieved during collection reported a last update of 25 September 2026.

## 3. Conceptual Definition

WGI defines Rule of Law as perceptions of the extent to which agents have confidence in and abide by the rules of society.

It particularly concerns:

- Contract enforcement.
- Property rights.
- The police.
- The courts.
- The likelihood of crime and violence.

The indicator is a broad perception-based measure of institutional quality and performance.

It does not directly measure government resources, the number of judges or police officers, judicial budgets, or administrative staffing.

Consequently, it should be interpreted as an indicator of institutional performance rather than a direct measurement of institutional capacity.

## 4. Selected Indicators

Six measurements were collected for each available country-year observation.

| Variable | World Bank API code | Description |
|---|---|---|
| RL Estimate | `GOV_WGI_RL.EST` | Governance estimate, approximately -2.5 to +2.5 |
| RL Score | `GOV_WGI_RL.SC` | Absolute governance score, 0–100 |
| RL Score Lower Bound | `GOV_WGI_RL.SC_LB` | Lower bound of the 90% confidence interval for the governance score |
| RL Score Upper Bound | `GOV_WGI_RL.SC_UB` | Upper bound of the 90% confidence interval for the governance score |
| RL Standard Error | `GOV_WGI_RL.SE` | Standard error of the governance estimate |
| RL Number of Sources | `GOV_WGI_RL.SR` | Number of underlying information sources |

### Interpretation

**Governance estimate:** Represents the country's estimated governance position in standard normal distribution units. Higher values indicate stronger perceived Rule of Law.

**Governance score:** Expresses the revised governance measurement on an absolute 0–100 scale. Higher values indicate stronger perceived Rule of Law.

**Confidence interval bounds:** Represent the lower and upper bounds of the 90% confidence interval for the absolute governance score.

**Standard error:** Indicates the precision of the governance estimate. Larger standard errors indicate greater uncertainty. A 90% confidence interval for the governance estimate can be approximated using:

Estimate ± (1.64 × Standard Error).

**Number of sources:** Indicates the number of underlying information sources contributing to the aggregate governance estimate. It is a contextual and data-quality variable, not a direct measure of institutional quality.

Note: The absolute governance score and percentile rank are different measurements. This dataset uses the absolute governance score, not percentile rank.

## 5. Geographical and Historical Coverage

The dataset covers all 11 current ASEAN member countries:

| Country | ISO-3 code |
|---|---|
| Brunei Darussalam | BRN |
| Cambodia | KHM |
| Indonesia | IDN |
| Lao PDR | LAO |
| Malaysia | MYS |
| Myanmar | MMR |
| Philippines | PHL |
| Singapore | SGP |
| Thailand | THA |
| Timor-Leste | TLS |
| Vietnam | VNM |

The research period is 1996–2024.

WGI observations are not annual throughout the entire period. The available reporting years are:

1996, 1998, 2000, and annually from 2002 through 2024.

This produces 26 reporting periods per country.

No interpolation was performed for years without WGI observations.

## 6. Data Collection and Processing

The dataset was collected using Python and the `requests` library to access the World Bank API.

The processing workflow consisted of:

1. Defining the 11 ASEAN countries using ISO-3 country codes.
2. Defining the six WGI Rule of Law indicators.
3. Retrieving observations for each country and indicator.
4. Storing the API observations in Python dictionaries.
5. Combining the observations into a Pandas DataFrame.
6. Grouping observations by country, country code, and year.
7. Combining the six measurements into one country-year record.
8. Sorting observations by country code and year.
9. Checking missing values, duplicate records, country coverage, and confidence interval consistency.
10. Exporting the processed dataset as a CSV file.

The final dataset contains the following columns:

- Country
- Country Code
- Year
- RL Estimate
- RL Score
- RL Score Lower Bound
- RL Score Upper Bound
- RL Standard Error
- RL Number of Sources

## 7. Data Quality and Validation

The final dataset contains:

| Measurement | Result |
|---|---:|
| ASEAN countries | 11 |
| Reporting periods per country | 26 |
| Total country-year records | 286 |
| Total indicator observations available | 1,704 |
| Missing indicator observations | 12 |
| Duplicate country-year records | 0 |
| Invalid confidence intervals | 0 |

### Missing Observations

Two country-year observations are missing for all six indicators:

| Country | Year | Missing measurements |
|---|---:|---:|
| Timor-Leste | 1996 | All six indicators |
| Timor-Leste | 1998 | All six indicators |

These observations were retained as missing values rather than replaced with zero or interpolated estimates.

The reason for their absence was not established during the API collection process.

All other 284 country-year records contain the six WGI measurements.

## 8. Methodological Considerations and Limitations

### Perception-Based Measurement

WGI aggregates perceptions from multiple underlying sources, including surveys and expert assessments.

Consequently, its estimates reflect perceptions of institutional quality rather than direct administrative measurements of government performance.

### Composite Indicator

Rule of Law is a broad aggregate measure covering several institutional and societal dimensions.

It does not independently identify the specific institutional weaknesses responsible for a country's score.

### Measurement Uncertainty

WGI estimates contain uncertainty.

Small differences between countries or changes over time should not automatically be interpreted as meaningful improvements or deteriorations.

The standard errors and confidence intervals should be considered when interpreting comparisons.

### Variation in Underlying Sources

The number and composition of underlying information sources may vary across countries and reporting years.

This can affect comparability and should be considered when analysing historical trends.

### Methodological Revisions

The revised WGI series recalculates historical estimates using its updated methodology.

The project therefore uses Source ID 3 consistently rather than combining observations from different WGI source versions.

### Overlap with WJP

WGI incorporates information from the World Justice Project among its underlying sources.

The Observatory also collects WJP Rule of Law data independently.

Therefore, WGI and WJP should not be treated as entirely independent confirmations of institutional quality.

WGI is used as a broad institutional comparison measure, while selected WJP subfactors provide more detailed diagnostic information concerning civil justice, criminal justice, judicial constraints, and public security.

## 9. Intended Use in the ASEAN Economic Observatory

The WGI Rule of Law dataset is classified under:

**Level 1 — Government and Institutional Environment**

**Dimension 1A — Institutional Quality**

**Subdimension 1A.1 — Rule of Law**

It will primarily support:

- Historical comparison of Rule of Law across ASEAN countries.
- Examination of Indonesia's institutional position within ASEAN.
- Analysis of the relationship between institutional quality and economic and social outcomes.
- Comparison with more specific judicial and public-security indicators from WJP.
- Subsequent investigation of relationships between institutional quality, public investment, and financial development.

The dataset is intended for descriptive and correlational analysis. Associations should not automatically be interpreted as causal relationships.

## 10. Output File

**Filename:** `asean_wgi_rule_of_law_1996_2024.csv`

**Location:** `data/processed/`

**Format:** CSV

**Processing script:** `wgi_rule_of_law.py`

**Status:** Data collection, processing, and initial validation completed.