def profitability(df):
    total_interest = df['Interest_Income'].sum()

    by_purpose = df.groupby('Loan_Amount')['Interest_Income'].sum()

    return {
        "total_interest": total_interest,
        "by_amount": by_purpose.head()
    }