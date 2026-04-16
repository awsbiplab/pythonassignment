import pandas as pd

def disbursement_efficiency(df):

    print("\n⏱️ LOAN DISBURSEMENT EFFICIENCY")

    results = {}

    # -----------------------------------
    # 1. PROCESSING TIME
    # -----------------------------------
    if 'APPLICATION_DATE' in df.columns and 'DISBURSAL_DATE' in df.columns:

        df['APPLICATION_DATE'] = pd.to_datetime(df['APPLICATION_DATE'], errors='coerce')
        df['DISBURSAL_DATE'] = pd.to_datetime(df['DISBURSAL_DATE'], errors='coerce')

        df['PROCESSING_DAYS'] = (
            df['DISBURSAL_DATE'] - df['APPLICATION_DATE']
        ).dt.days

        avg_time = df['PROCESSING_DAYS'].mean()

        print(f"\n📊 Average Processing Time: {avg_time:.2f} days")

        results['avg_time'] = avg_time

    else:
        print("⚠️ Missing date columns")

    # -----------------------------------
    # 2. REGION COMPARISON (ALTERNATIVE)
    # -----------------------------------
    if 'REGION' in df.columns:

        region_time = df.groupby('REGION')['PROCESSING_DAYS'].mean()

        print("\n📊 Processing Time by Region:\n", region_time)

        results['region_time'] = region_time

    # -----------------------------------
    # 3. LOAN PURPOSE ANALYSIS
    # -----------------------------------
    purpose_col = None

    for col in df.columns:
        if 'PURPOSE' in col.upper():
            purpose_col = col
            break

    if purpose_col:

        purpose_time = df.groupby(purpose_col)['PROCESSING_DAYS'].mean()

        print(f"\n📊 Processing Time by {purpose_col}:\n", purpose_time)

        results['purpose'] = purpose_time

    else:
        print("⚠️ Loan purpose column not available")

    # -----------------------------------
    # 🚨 BRANCH LIMITATION
    # -----------------------------------
    print("\n⚠️ Branch comparison NOT possible")
    print("Reason: No BRANCH_ID linkage in dataset")

    return results