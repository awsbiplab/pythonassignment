import pandas as pd

def recovery_effectiveness(df):

    print("\nRECOVERY EFFECTIVENESS")

    results = {}

    # -----------------------------------
    # 1. HANDLE MISSING VALUES
    # -----------------------------------
    df['DEFAULT_AMOUNT'] = df['DEFAULT_AMOUNT'].fillna(0)
    df['RECOVERY_AMOUNT'] = df['RECOVERY_AMOUNT'].fillna(0)

    # -----------------------------------
    # 2. FILTER VALID DEFAULT CASES
    # -----------------------------------
    df_valid = df[df['DEFAULT_AMOUNT'] > 0].copy()

    if df_valid.empty:
        print("No valid default data")
        return results

    # -----------------------------------
    # 3. CALCULATE RECOVERY RATE
    # -----------------------------------
    df_valid['RECOVERY_RATE'] = (
        df_valid['RECOVERY_AMOUNT'] / df_valid['DEFAULT_AMOUNT']
    )

    # -----------------------------------
    # 4. OVERALL RECOVERY EFFECTIVENESS
    # -----------------------------------
    overall_rate = df_valid['RECOVERY_RATE'].mean()

    print(f"\n Overall Recovery Rate: {overall_rate:.2f}")

    results['overall'] = overall_rate

    # -----------------------------------
    # 5. LEGAL ACTION COMPARISON
    # -----------------------------------
    if 'LEGAL_ACTION' in df_valid.columns:

        legal_group = df_valid.groupby('LEGAL_ACTION')['RECOVERY_RATE'].mean()

        print("\n Recovery Rate by Legal Action:\n", legal_group)

        results['legal'] = legal_group

    else:
        print(" LEGAL_ACTION column missing")

    return results