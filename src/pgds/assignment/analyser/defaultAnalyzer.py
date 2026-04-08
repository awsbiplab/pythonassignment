def defaultMetrics(df):
    default_rate = df['Default_Flag'].mean()

    by_credit = df.groupby('Credit_Score')['Default_Flag'].mean()

    return {
        "default_rate": default_rate,
        "credit_risk": by_credit.describe()
    }