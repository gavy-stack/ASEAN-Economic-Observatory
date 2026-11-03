# WJP Rule of Law Dataset
## ASEAN Economic Observatory

**Dataset:** World Justice Project (WJP) Rule of Law Index — Historical Data  
**Framework placement:** Level 1 — Government and Institutional Environment  
**Subdimension:** 1A.1 — Rule of Law  
**Research period:** 2012–2024  
**Documentation version:** 1.0  
**Status:** Initial data preparation completed

---

## 1. Purpose

This dataset supports the examination of the rule of law across ASEAN countries as part of the ASEAN Economic Observatory.

It focuses on three analytical dimensions:

1. Civil Justice
2. Criminal Justice
3. Judicial Checks and Public Security

The dataset is intended to help assess the effectiveness of judicial institutions, access to justice, the administration of criminal justice, judicial constraints on government power, and public security.

The WJP indicators primarily capture institutional performance and the experiences or perceptions reflected in the index. They should not be interpreted as direct measurements of government resources, staffing, budgets, or administrative capacity.

## 2. Data Source

**Source:** World Justice Project (WJP), Rule of Law Index — Historical Data.

**Original file:** `wjp_historical.xlsx`  
**Source worksheet:** `Historical Data`  
**Raw data location:** `data/raw/wjp_historical.xlsx`

The historical workbook contains the overall Rule of Law Index, eight factors, and 44 subfactors.

The consolidated historical worksheet was selected because it provides a structured dataset containing historical observations across countries and reporting periods.

WJP scores are expressed on a scale from 0 to 1, with higher scores generally indicating stronger performance in the respective dimension.

## 3. Geographical Coverage

The research framework covers all 11 current ASEAN member countries. However, the WJP historical dataset contains observations for only eight of them.

| Country | ISO Code | WJP Coverage |
|---|---|---|
| Cambodia | KHM | Available |
| Indonesia | IDN | Available |
| Malaysia | MYS | Available |
| Myanmar | MMR | Available from 2014 |
| Philippines | PHL | Available |
| Singapore | SGP | Available |
| Thailand | THA | Available |
| Vietnam | VNM | Available |
| Brunei Darussalam | BRN | Not available |
| Lao PDR | LAO | Not available |
| Timor-Leste | TLS | Not available |

The absence of observations for three countries represents a data coverage limitation. Missing country coverage is not interpreted as zero performance.

## 4. Historical Coverage

The dataset covers the following 11 reporting periods:

- 2012–2013
- 2014
- 2015
- 2016
- 2017–2018
- 2019
- 2020
- 2021
- 2022
- 2023
- 2024

The periods 2012–2013 and 2017–2018 represent combined reporting periods rather than separate annual observations.

Consequently, the dataset contains:

- Seven countries with 11 reporting periods each.
- Myanmar with 10 reporting periods, beginning in 2014.
- Eight countries in total.
- 87 country-period observations.

These reporting periods are preserved in their original form. Combined-period observations are not duplicated or artificially converted into annual observations.

## 5. Indicator Selection

A total of 19 indicators were selected from the WJP historical dataset.

They are organised into three analytical groups.

### 5.1 Civil Justice

The first group contains Factor 7 and all seven of its subfactors.

| Code | Indicator |
|---|---|
| Factor 7 | Civil Justice |
| 7.1 | People can access and afford civil justice |
| 7.2 | Civil justice is free of discrimination |
| 7.3 | Civil justice is free of corruption |
| 7.4 | Civil justice is free of improper government influence |
| 7.5 | Civil justice is not subject to unreasonable delay |
| 7.6 | Civil justice is effectively enforced |
| 7.7 | Alternative dispute resolution mechanisms are accessible, impartial, and effective |

### 5.2 Criminal Justice

The second group contains Factor 8 and all seven of its subfactors.

| Code | Indicator |
|---|---|
| Factor 8 | Criminal Justice |
| 8.1 | Criminal investigation system is effective |
| 8.2 | Criminal adjudication system is timely and effective |
| 8.3 | Correctional system is effective in reducing criminal behavior |
| 8.4 | Criminal system is impartial |
| 8.5 | Criminal system is free of corruption |
| 8.6 | Criminal system is free of improper government influence |
| 8.7 | Due process of the law and rights of the accused |

### 5.3 Judicial Checks and Public Security

The third group contains three supplementary indicators.

| Code | Indicator |
|---|---|
| 1.2 | Government powers are effectively limited by the judiciary |
| 5.1 | Crime is effectively controlled |
| 5.2 | Civil conflict is effectively limited |

These supplementary indicators provide additional information about judicial constraints on government power and the effectiveness of public security.

### Indicator Selection Rationale

Civil Justice and Criminal Justice are retained as the primary judicial-performance dimensions.

The supplementary indicators broaden the analysis by incorporating judicial checks on government authority and public security.

The three groups are maintained separately for analytical clarity. They are not automatically combined into one composite Rule of Law score.

Parent factor scores are retained alongside their subfactor scores for reference. Parent scores and their constituent subfactors must not be averaged together, as this would risk double-counting the same underlying information.

## 6. Data Processing

Data preparation was conducted using Python and pandas.

The processing script is:

`wjp_rule_of_law.py`

The following procedures were applied:

1. Loaded the `Historical Data` worksheet from the original Excel workbook.
2. Selected the four metadata fields: Country, Year, Country Code, and Region.
3. Extracted the 19 selected Rule of Law indicators.
4. Filtered observations using the ISO country codes of the 11 ASEAN members.
5. Restricted the dataset to the reporting periods from 2012–2013 through 2024.
6. Converted the Year field to strings to preserve combined reporting-period labels.
7. Inspected missing values across all selected indicators.
8. Sorted observations by country code and reporting period.
9. Exported the resulting dataset to CSV format.

The original Excel workbook remains preserved in `data/raw/`. Processing was performed on a separate DataFrame, leaving the original source data unchanged.

## 7. Data Quality and Coverage Assessment

### 7.1 Dataset Structure

| Attribute | Result |
|---|---:|
| Country-period observations | 87 |
| Countries | 8 |
| Selected indicators | 19 |
| Metadata fields | 4 |
| Total columns | 23 |
| Possible indicator scores | 1,653 |
| Available indicator scores | 1,651 |
| Missing indicator scores | 2 |
| Indicator availability | 99.88% |

### 7.2 Missing Values

Two missing scores were identified.

Both belong to indicator 8.3: Correctional system effectiveness.

| Country | Indicator | Missing observations |
|---|---|---:|
| Indonesia | 8.3 | 1 |
| Myanmar | 8.3 | 1 |

Missing observations are preserved as missing values. They are not replaced with zero, estimated, or imputed.

### 7.3 Historical Data Validation

The consolidated historical worksheet was compared with the original 2012–2013 worksheet.

The validation covered 19 selected indicators across 97 countries.

| Validation result | Count |
|---|---:|
| Total comparisons | 1,843 |
| Matching scores | 1,843 |
| Mismatching scores | 0 |

This confirms that the numerical values for the selected indicators were correctly preserved and mapped in the consolidated historical dataset for the 2012–2013 period.

However, numerical agreement does not establish that indicator definitions or measurement methodologies remained unchanged across all subsequent editions.

## 8. Methodological Limitations

Several limitations must be considered when using this dataset.

### 8.1 Incomplete ASEAN Coverage

Only eight of the 11 ASEAN countries are represented. Results from this dataset cannot automatically be interpreted as representative of the entire ASEAN region.

### 8.2 Non-Annual Reporting Periods

The historical observations include combined reporting periods. They cannot be treated as a fully annual time series without an explicit and justified methodology.

### 8.3 Methodological Revisions

WJP has revised its methodology and historical scores across different editions. The workbook also documents revisions affecting earlier index editions.

Comparisons across reporting periods should therefore account for changes in methodology and indicator definitions.

### 8.4 Indicator Definition Changes

Historical subfactor labels and definitions have changed over time. In particular, some 2012–2013 indicators were measured using different questions from those used in later editions.

The consolidated worksheet may present historical scores under later labels. Consequently, the numerical preservation of historical values should not be confused with conceptual consistency across periods.

### 8.5 Perception and Experience-Based Measurement

WJP indicators draw on surveys and other sources. They capture dimensions of institutional performance, public experience, and expert assessment, rather than providing direct administrative measurements of institutional resources or capacity.

### 8.6 Overlap with Other Governance Indicators

WJP indicators overlap conceptually with other parts of the Observatory framework.

For example:

- Factor 2 — Absence of Corruption relates to Level 1A.3, Control of Corruption.
- Factor 3 — Open Government relates to Level 1A.4, Accountability.
- Factor 6 — Regulatory Enforcement relates to Level 1A.2, Regulatory Quality.

These indicators are not included in this particular Rule of Law selection. Their potential use elsewhere in the framework should be evaluated separately to avoid double-counting.

## 9. Output Files

| File | Location | Purpose |
|---|---|---|
| Original WJP workbook | `data/raw/wjp_historical.xlsx` | Preserved source data |
| Python processing script | `wjp_rule_of_law.py` | Data extraction and processing |
| Cleaned dataset | `data/processed/asean_wjp_rule_of_law_2012_2024.csv` | Selected ASEAN Rule of Law observations |
| Historical validation | `data/processed/wjp_2012_2013_validation.csv` | Numerical validation against the original worksheet |

## 10. Intended Use in the Observatory

This dataset will support the analysis of Level 1A.1 — Rule of Law.

Potential applications include:

- Comparing civil justice performance across covered ASEAN countries.
- Examining criminal justice performance and its subdimensions.
- Assessing judicial constraints on government power.
- Examining the relationship between public security and economic development.
- Exploring relationships between judicial performance and other dimensions of government capacity.

The dataset may eventually be compared with World Governance Indicators and other institutional measures.

However, overlapping source material and differences in measurement methodology must be considered before combining or interpreting these indicators.

For integration with annual economic datasets, the original WJP reporting periods must be retained and an explicit temporal matching approach must be established.

---

**Documentation status:** Initial dataset preparation completed.  
**Next stage:** Further indicator research, methodological review, and integration with other Observatory datasets.