#def default_risk_analysis(df): return df.groupby('DEFAULT_FLAG').mean(numeric_only=True)

import pandas as pd

def default_risk_analysis(df, branches=None):
    print("\n⚠️ DEFAULT RISK ANALYSIS")

    results = {}

    # -----------------------------------
    # 1. CORRELATION: LOAN ATTRIBUTES
    # -----------------------------------
    cols = ['LOAN_AMOUNT', 'INTEREST_RATE', 'CREDIT_SCORE', 'DEFAULT_FLAG']

    available_cols = [c for c in cols if c in df.columns]

    if len(available_cols) >= 2:
        corr = df[available_cols].corr()
        results['loan_correlation'] = corr
        print("\nLoan Attribute Correlation:\n", corr)

    # -----------------------------------
    # 2. PAIRWISE CORRELATION
    # -----------------------------------
    pair_cols = ['EMI_AMOUNT', 'OVERDUE_AMOUNT', 'DEFAULT_AMOUNT']

    pair_cols = [c for c in pair_cols if c in df.columns]

    if len(pair_cols) >= 2:
        pair_corr = df[pair_cols].corr()
        results['pairwise_correlation'] = pair_corr
        print("\nPairwise Correlation:\n", pair_corr)

    # -----------------------------------
    # 3. BRANCH-LEVEL DEFAULT ANALYSIS
    # -----------------------------------
    if branches is not None and 'BRANCH_ID' in df.columns:
        merged = df.merge(branches, on='BRANCH_ID', how='left')

        branch_corr = merged.groupby('REGION').agg({
            'DEFAULT_FLAG': 'mean',
            'DELINQUENT_LOANS': 'mean',
            'LOAN_DISBURSEMENT_AMOUNT': 'mean'
        })

        results['branch_analysis'] = branch_corr
        print("\nBranch-Level Risk:\n", branch_corr)

    return results