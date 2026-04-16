import pandas as pd

def time_series_analysis(df):

    print("\n TIME SERIES ANALYSIS")

    results = {}

    # -----------------------------------
    # 1. MONTHLY DISBURSEMENT TREND
    # -----------------------------------
    if 'DISBURSAL_DATE' in df.columns:

        df['DISBURSAL_DATE'] = pd.to_datetime(df['DISBURSAL_DATE'], errors='coerce')

        disb_trend = df.groupby(
            df['DISBURSAL_DATE'].dt.to_period('M')
        ).size()

        print("\n Monthly Disbursement Trend:\n", disb_trend.head())

        results['disbursement'] = disb_trend

    else:
        print(" DISBURSAL_DATE missing")

    # -----------------------------------
    # 2. SEASONAL PATTERN (APPLICATIONS)
    # -----------------------------------
    if 'APPLICATION_DATE' in df.columns:

        df['APPLICATION_DATE'] = pd.to_datetime(df['APPLICATION_DATE'], errors='coerce')

        seasonal_app = df.groupby(
            df['APPLICATION_DATE'].dt.month
        ).size()

        print("\n Seasonal Pattern (Applications):\n", seasonal_app)

        results['seasonal_app'] = seasonal_app

    # -----------------------------------
    # SEASONAL PATTERN (DISBURSEMENT)
    # -----------------------------------
    if 'DISBURSAL_DATE' in df.columns:

        seasonal_disb = df.groupby(
            df['DISBURSAL_DATE'].dt.month
        ).size()

        print("\n Seasonal Pattern (Disbursement):\n", seasonal_disb)

        results['seasonal_disb'] = seasonal_disb

    # -----------------------------------
    # 3. DEFAULT RATE BY REGION (NOT DOABLE)
    # -----------------------------------
    print("\n Monthly default rate by region NOT possible")
    print("Reason: DEFAULT_DATE column not available in dataset")

    return results