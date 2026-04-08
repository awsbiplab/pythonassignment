import pandas as pd

def emi_analysis(df):
    print("\n💰 EMI ANALYSIS")

    results = {}

    # -----------------------------------
    # 1. EMI vs DEFAULT PROBABILITY
    # -----------------------------------
    if 'EMI_AMOUNT' in df.columns:
        emi_default = df.groupby('EMI_AMOUNT')['DEFAULT_FLAG'].mean()

        results['emi_vs_default'] = emi_default

        print("\nEMI vs Default Probability:\n", emi_default.head())

    # -----------------------------------
    # 2. EMI THRESHOLD ANALYSIS
    # -----------------------------------
    if 'EMI_AMOUNT' in df.columns:
        df['EMI_BUCKET'] = pd.qcut(df['EMI_AMOUNT'], q=5, duplicates='drop')

        threshold = df.groupby('EMI_BUCKET')['DEFAULT_FLAG'].mean()

        results['emi_threshold'] = threshold

        print("\nEMI Threshold Analysis:\n", threshold)

    # -----------------------------------
    # 3. EMI BY LOAN TYPE
    # -----------------------------------
    if 'LOAN_TYPE' in df.columns:
        emi_by_type = df.groupby('LOAN_TYPE')['EMI_AMOUNT'].mean()

        results['emi_by_type'] = emi_by_type

        print("\nEMI by Loan Type:\n", emi_by_type)

    return results