
import requests


# --------------------------------------------------
# CONFIGURATION
# --------------------------------------------------

COUNTRY_CODE = "IDN"
START_YEAR = 1996
END_YEAR = 2024
SOURCE_ID = 3

INDICATORS = {
    "Estimate": "GOV_WGI_RQ.EST",
    "Score": "GOV_WGI_RQ.SC",
    "Score Lower Bound": "GOV_WGI_RQ.SC_LB",
    "Score Upper Bound": "GOV_WGI_RQ.SC_UB",
    "Standard Error": "GOV_WGI_RQ.SE",
    "Number of Sources": "GOV_WGI_RQ.SR",
}


# --------------------------------------------------
# FUNCTION 1: CHECK ONE INDICATOR
# --------------------------------------------------

def check_indicator(session, name, indicator_id):

    url = (
        f"https://api.worldbank.org/v2/country/"
        f"{COUNTRY_CODE}/indicator/{indicator_id}"
    )

    params = {
        "date": f"{START_YEAR}:{END_YEAR}",
        "format": "json",
        "per_page": 100,
        "source": SOURCE_ID
    }

    try:
        response = session.get(url, params=params, timeout=30)
        response.raise_for_status()

        data = response.json()

        if not isinstance(data, list) or len(data) < 2:
            raise ValueError(f"Unexpected API response: {data}")

        metadata = data[0]
        observations = data[1] or []

        # Verify the returned indicator ID
        if observations:
            returned_id = observations[0]["indicator"]["id"]

            if returned_id != indicator_id:
                raise ValueError(
                    f"Indicator mismatch: expected {indicator_id}, "
                    f"received {returned_id}"
                )

        # Identify available years
        available_years = {
            int(obs["date"])
            for obs in observations
        }

        # Identify missing years
        expected_years = set(range(START_YEAR, END_YEAR + 1))

        missing_years = sorted(
            expected_years - available_years
        )

        return {
            "name": name,
            "indicator_id": indicator_id,
            "status": response.status_code,
            "last_updated": metadata.get("lastupdated"),
            "total": metadata.get("total"),
            "observations": len(observations),
            "missing_years": missing_years,
            "error": None
        }

    except (requests.RequestException, ValueError, KeyError, TypeError) as error:

        return {
            "name": name,
            "indicator_id": indicator_id,
            "status": "FAILED",
            "last_updated": None,
            "total": None,
            "observations": 0,
            "missing_years": None,
            "error": str(error)
        }


# --------------------------------------------------
# FUNCTION 2: CHECK ALL SIX INDICATORS
# --------------------------------------------------

def check_all_indicators():

    print("=" * 65)
    print("WGI REGULATORY QUALITY — API VALIDATION")
    print("=" * 65)

    print(f"Country: {COUNTRY_CODE}")
    print(f"Period: {START_YEAR}-{END_YEAR}")
    print(f"Expected years: {END_YEAR - START_YEAR + 1}")
    print()

    results = []

    with requests.Session() as session:

        for name, indicator_id in INDICATORS.items():

            print(f"Checking {name}...")

            result = check_indicator(
                session,
                name,
                indicator_id
            )

            results.append(result)

    # Print consolidated results
    print("\n" + "=" * 65)
    print("VALIDATION SUMMARY")
    print("=" * 65)

    for result in results:

        print(f"\n{result['name']}")
        print(f"Indicator ID: {result['indicator_id']}")
        print(f"HTTP Status: {result['status']}")

        if result["error"] is not None:
            print(f"Error: {result['error']}")
            continue

        print(f"Last Updated: {result['last_updated']}")
        print(f"Observations: {result['observations']}")
        print(f"Missing Years: {result['missing_years']}")

    return results


# --------------------------------------------------
# EXECUTION
# --------------------------------------------------

if __name__ == "__main__":
    results = check_all_indicators()
