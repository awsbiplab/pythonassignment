import pandas as pd
def time_series(df):
    df['TRANSACTION_DATE']=pd.to_datetime(df['TRANSACTION_DATE'])
    return df.groupby(df['TRANSACTION_DATE'].dt.month).size()