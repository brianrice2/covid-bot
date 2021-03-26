import pandas as pd

url = 'https://raw.githubusercontent.com/nytimes/covid-19-data/master/us.csv'

if __name__ == '__main__':
    # pull COVID data from NYT Github
    df = pd.read_csv(url)

    # clean and engineer
    df['date'] = pd.to_datetime(df['date'])
    df['daily_cases'] = df['cases'] - df['cases'].shift(1, fill_value=0)
    df['daily_deaths'] = df['deaths'] - df['deaths'].shift(1, fill_value=0)

    # print daily cases and deaths
    daily_stats = df.tail(1).loc[:, ['date', 'daily_cases', 'daily_deaths']].to_dict(orient='records')[0]
    print(
        daily_stats['date'].strftime('%B %d, %Y'), ': ',
        daily_stats['daily_cases'], ' cases, ',
        daily_stats['daily_deaths'], ' deaths',
        sep=''
    )
