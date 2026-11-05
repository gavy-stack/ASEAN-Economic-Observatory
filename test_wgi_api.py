import requests

countries = {
    "Brunei Darussalam": "BRN",
    "Cambodia": "KHM",
    "Indonesia": "IDN",
    "Lao PDR": "LAO",
    "Malaysia": "MYS",
    "Myanmar": "MMR",
    "Philippines": "PHL",
    "Singapore": "SGP",
    "Thailand": "THA",
    "Timor-Leste": "TLS",
    "Vietnam": "VNM"
}

indicators = {
    "RQ Estimate": "GOV_WGI_RQ.EST",
    "RQ Score": "GOV_WGI_RQ.SC",
    "RQ Score Lower Bound": "GOV_WGI_RQ.SC_LB",
    "RQ Score Upper Bound": "GOV_WGI_RQ.SC_UB",
    "RQ Standard Error": "GOV_WGI_RQ.SE",
    "RQ Number of Sources": "GOV_WGI_RQ.SR"
}

for country_name, country_code in countries.items():

    print(f"\n========== {country_name} ({country_code}) ==========")

    for indicator_name, indicator_code in indicators.items():

        url = (
            f"https://api.worldbank.org/v2/country/{country_code}/"
            f"indicator/{indicator_code}"
        )

        params = {
            "date": "1996:2024",
            "format": "json",
            "per_page": 100,
            "source": 3
        }

        response = requests.get(url, params=params, timeout=30)

        if response.status_code != 200:
            print(indicator_name, "- HTTP ERROR:", response.status_code)
            continue

        data = response.json()

        if not isinstance(data, list) or len(data) < 2:
            print(indicator_name, "- INVALID API RESPONSE")
            continue

        observations = data[1]

        returned_countries = {
            item["countryiso3code"] for item in observations
        }

        returned_indicators = {
            item["indicator"]["id"] for item in observations
        }

        years = sorted({
            int(item["date"]) for item in observations
        })

        country_check = returned_countries == {country_code}
        indicator_check = returned_indicators == {indicator_code}

        print(
            f"{indicator_name}: "
            f"HTTP {response.status_code} | "
            f"Observations: {len(observations)} | "
            f"Country: {'PASS' if country_check else 'FAIL'} | "
            f"Indicator: {'PASS' if indicator_check else 'FAIL'} | "
            f"Years: {years}"
        )