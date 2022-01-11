import pandas as pd

url = "https://raw.githubusercontent.com/nytimes/covid-19-data/master/us.csv"


def main():
    # Pull COVID data from NYT Github
    df = pd.read_csv(url)

    # Clean and engineer features
    df["date"] = pd.to_datetime(df["date"])
    df["daily_cases"] = df["cases"] - df["cases"].shift(1, fill_value=0)
    df["daily_deaths"] = df["deaths"] - df["deaths"].shift(1, fill_value=0)

    # Print daily cases and deaths
    daily_stats = (
        df.tail(1).loc[:, ["date", "daily_cases", "daily_deaths"]].to_dict(orient="records")[0]
    )
    print(
        f"""
        {daily_stats["date"].strftime("%B %d, %Y")}:
        {daily_stats["daily_cases"]:,} cases
        {daily_stats["daily_deaths"]:,} deaths
        """
    )


if __name__ == "__main__":
    main()
