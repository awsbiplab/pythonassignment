import pandas as pd

def customer_segmentation(df):
    print("\n👥 CUSTOMER SEGMENTATION")

    # -----------------------------------
    # 1. CREDIT SCORE SEGMENT
    # -----------------------------------
    df['CREDIT_SEGMENT'] = pd.cut(
        df['CREDIT_SCORE'],
        bins=[0, 500, 650, 750, 900],
        labels=['High Risk', 'Medium', 'Good', 'Excellent']
    )

    # -----------------------------------
    # 2. INCOME SEGMENT
    # -----------------------------------
    df['INCOME_SEGMENT'] = pd.qcut(
        df['ANNUAL_INCOME'],
        q=3,
        labels=['Low Income', 'Mid Income', 'High Income']
    )

    # -----------------------------------
    # 3. LOAN STATUS SEGMENT
    # -----------------------------------
    df['LOAN_STATUS'] = df['DEFAULT_FLAG'].map({
        0: 'Active',
        1: 'Default'
    })

    # -----------------------------------
    # 4. HIGH-RISK CUSTOMERS
    # -----------------------------------
    high_risk = df[
        (df['CREDIT_SEGMENT'] == 'High Risk') |
        (df['DEFAULT_FLAG'] == 1)
    ]

    # -----------------------------------
    # 5. HIGH-VALUE CUSTOMERS
    # -----------------------------------
    high_value = df[
        (df['CREDIT_SEGMENT'].isin(['Good', 'Excellent'])) &
        (df['INCOME_SEGMENT'] == 'High Income') &
        (df['DEFAULT_FLAG'] == 0)
    ]

    # -----------------------------------
    # 6. REPAYMENT BEHAVIOR
    # -----------------------------------
    behavior = df.groupby('CREDIT_SEGMENT')['DEFAULT_FLAG'].mean()

    print("\nHigh Risk Customers:", len(high_risk))
    print("High Value Customers:", len(high_value))

    print("\nRepayment Behavior:\n", behavior)

    return {
        "df": df,
        "high_risk": high_risk,
        "high_value": high_value,
        "behavior": behavior
    }