# WGI Rule of Law Dataset

## 1. Purpose
This dataset measures the broad institutional quality and performance of Rule of Law across ASEAN countries. It serves as the primary comparative indicator for Level 1A.1 — Rule of Law in the ASEAN Economic Observatory.

## 2. Data Source
- Source: World Bank — Worldwide Governance Indicators (WGI).
- API: World Bank Indicators API.
- Source ID: `3` (revised WGI series).
- Historical period: 1996–2024.
- Latest source metadata update at collection: 2026-09-25.

## 3. Selected Indicators
- RL Estimate (`GOV_WGI_RL.EST`): Rule of Law estimate in standard normal units (approximately -2.5 to +2.5).
- RL Score (`GOV_WGI_RL.SC`): Absolute governance score on a 0–100 scale.
- RL Score Lower Bound (`GOV_WGI_RL.SC_LB`): Lower bound of the 90% confidence interval for the score.
- RL Score Upper Bound (`GOV_WGI_RL.SC_UB`): Upper bound of the 90% confidence interval for the score.
- RL Standard Error (`GOV_WGI_RL.SE`): Standard error of the governance estimate.
- RL Number of Sources (`GOV_WGI_RL.SR`): Number of underlying data sources used for the estimate.

## 4. Geographical and Historical Coverage
- Countries: All 11 ASEAN member states.
- Reporting periods: 26 per country (1996, 1998, 2000, and annually from 2002 to 2024).
- Total country-year records: 286.
- Missing observations: Timor-Leste, 1996 and 1998 (all six indicators).
- Available indicator observations: 1,704 out of 1,716 (99.3%).

## 5. Processing and Validation
Data was collected using Python and the World Bank API, then organised by country code and year.
- Duplicate country-year records: 0.
- Invalid confidence intervals: 0.
- Missing values were retained as missing (`NaN`), not replaced with zero.
- The six indicators were combined into one country-year dataset.

## 6. Methodological Considerations
WGI measures perceptions of Rule of Law, including confidence in and adherence to societal rules, contract enforcement, property rights, police, courts, and crime and violence.

WGI aggregates information from multiple surveys and expert assessments using an Unobserved Components Model (UCM). Its results are estimates, not direct measurements of government resources or administrative capacity.

Scores should be interpreted with their uncertainty intervals. Small differences between countries or years should not automatically be treated as meaningful.

WGI also uses some WJP information as an underlying source; therefore, WGI and WJP should not be treated as fully independent measures.

## 7. Output
`data/processed/asean_wgi_rule_of_law_1996_2024.csv`

The dataset supports regional comparison and descriptive analysis of institutional quality. It does not, by itself, establish causal relationships.