import pandas as pd

def descriptive_analysis(df, applications=None):
    results = {}

    print("\n📊 DESCRIPTIVE ANALYSIS")

    # -----------------------------
    # 1. DISTRIBUTIONS
    # -----------------------------
    results['loan_amount_stats'] = df['LOAN_AMOUNT'].describe()

    if 'EMI_AMOUNT' in df.columns:
        results['emi_stats'] = df['EMI_AMOUNT'].describe()

    results['credit_score_stats'] = df['CREDIT_SCORE'].describe()

    # -----------------------------
    # 2. REGIONAL TRENDS
    # -----------------------------
    if 'REGION' in df.columns:
        regional = df.groupby('REGION').agg({
            'LOAN_AMOUNT': 'sum',
            'DEFAULT_FLAG': 'mean'
        }).rename(columns={
            'LOAN_AMOUNT': 'TOTAL_DISBURSEMENT',
            'DEFAULT_FLAG': 'DEFAULT_RATE'
        })

        results['regional_trends'] = regional

    # -----------------------------
    # 3. MONTHLY TRENDS
    # -----------------------------
    if applications is not None and 'APPLICATION_DATE' in applications.columns:
        applications['APPLICATION_DATE'] = pd.to_datetime(
            applications['APPLICATION_DATE'], errors='coerce'
        )

        monthly = applications.groupby(
            applications['APPLICATION_DATE'].dt.to_period('M')
        ).size()

        results['monthly_applications'] = monthly

    return results