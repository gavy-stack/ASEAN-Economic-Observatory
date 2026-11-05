Hi, this is the official documentation of Regulatory Quality data retrieval from World Governance Inidcator (WGI) from World Bank.

We put our focus solely on Indonesia and its surrounding South East Asian neighbor.

We used 1996-2024 as our timeline.

WGI published several versions of the dataset. We used the 3rd version called Source 3.

The indicators used are:
    - Regulatory Quality Estimate, Governance estimate on an approximately −2.5 to +2.5 scale.
    - Regulatory Quality Score, Standardised score on a 0–100 scale
    - Regulatory Quality Score Lower Bound, Lower limit of the score's confidence interval.
    - Regulatory Quality Score Upper Bound, Upper limit of the score's confidence interval.
    - Regulatory Quality Standard Error, Indicates statistical uncertainty around the estimate.
    - Regulatory Quality Number of Sources, Number of underlying data sources contributing to the measurement.

Here are our current worfklows:
1. API Data collection ✅
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
7. Last Validation for the proccessed dataset✅
    Confidence intervals ✅, score consistency ✅, standard errors✅, source counts ✅, checking whether all 6 indicators missing values are identical ✅

Explanation
    The result of the proccessed dataset
        In the proccessed asean_wgi_regulatory_quality_1996_2024.csv file, there are total of 319 values. We called these as country-year combination because it combines 11 countries of ASEAN and 29 years of observation period (11*29=319)

        To put it simply, the supposed available data is 1,914 from 29 years of observation x 11 countries of asean x total 6 indicators right? 
        
        However, as reality hits, the official source records only 26 years of observation, since 1997, 1999, and 2001 are missing. Therefore, the raw dataset we collected only retreived 26 years observation, which reduces the available data to 1,716= 11 countries x 6 total indicators x 26 recorded years.

        But we also notice that some values in Timor Leste are missing. We see that the missing years are 1996, 1997, 1998, 1999,2000, 2001. Therefore,as each year hold 6 indicator , the total values missing are 6 indicator x 6 missing years= 36 missing values from Timor Leste

        1,716 missing values are already recorded the missing 3 years of observation. Therefore additional 3 years missing year from Timor Leste added 18 missing values. 1,716 - 18 = 1,698. Therefore the total values that are available here are 1,698 from the suppossed total of 1,914

        p.s.: Its too hard to explain clearly all of it. Just read the dataset or reach me out.

Limitations
    - As mentioned before some values are missing. 216 out of 1,914 possible indicator values are missing (11.29%).

    - The WGI Regulatory Quality is a perception based. It may be different from actual government performance because its based on perception.

    - WGI also combines from multiple underlying sources and the reusults depend on the available sources and their assessments.

