import pandas as pd
def processing_time(df):
    df['PROCESSING_DAYS']=(pd.to_datetime(df['APPROVAL_DATE'])-pd.to_datetime(df['APPLICATION_DATE'])).dt.days
    return df['PROCESSING_DAYS'].mean()