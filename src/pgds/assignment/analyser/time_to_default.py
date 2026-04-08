import pandas as pd
def time_to_default(df):
    df['TIME_TO_DEFAULT']=(pd.to_datetime(df['DEFAULT_DATE'])-pd.to_datetime(df['LOAN_START_DATE'])).dt.days
    return df['TIME_TO_DEFAULT'].mean()