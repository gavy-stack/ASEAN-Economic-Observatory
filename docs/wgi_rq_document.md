Hi, this is the official documentation of Regulatory Quality data retrieval from World Governance Inidcator (WGI) from World Bank.

We put our focus solely on Indonesia and its surrounding South East Asian neighbor.

We used 1996-2024 as our timeline.

WGI published several versions of the dataset. We used the 3rd version called Source 3.

Here are our current worfklows:
1. API Data collection
- Explanation: Retrieve the six WGI measurements for all 11 ASEAN countries.
    1.1. Test API response of Indonesia only ✅
        - Result HTTP response 200 ✅, Country Code IDN ✅, Indicator ID ✅, Source ID 3✅, Observations are 26 from expected 29 ✅, Year range 1996-2024 (1997, 1999, and 2001 are missing)✅
    1.2. Test API reponse of whole ASEAN (11 members)
        - Yes the API works and the whole 11 members have 3 years missing from the dataset ✅
2. Check the collected data ✅
    Confirm country codes, indicator IDs, years, and API responses.
3. Save raw data ✅
    Preserve the original downloaded observations.
4. Process the data ✅
    Combine the six measurements into one dataset with one row per country-year.
5. Validate the final dataset ✅
    Check missing values, duplicate records, country coverage, and confidence intervals.
6. Export the dataset ✅
    Save the final CSV in data/processed/.
7. Last Validation for the proccessed dataset
    Confidence intervals, score consistency, standard errors, source counts

