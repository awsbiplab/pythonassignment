import pandas as pd

def branch_performance(df, applications=None, defaults=None):
    print("\n🏢 BRANCH PERFORMANCE ANALYSIS")

    results = {}

    # -----------------------------------
    # 1. LOAN DISBURSEMENT + DEFAULT RATE
    # -----------------------------------
    if 'BRANCH_ID' in df.columns:
        branch_summary = df.groupby('BRANCH_ID').agg({
            'LOAN_AMOUNT': 'sum',
            'DEFAULT_FLAG': 'mean'
        }).rename(columns={
            'LOAN_AMOUNT': 'TOTAL_DISBURSEMENT',
            'DEFAULT_FLAG': 'DEFAULT_RATE'
        })

        results['branch_summary'] = branch_summary
        print("\nBranch Summary:\n", branch_summary.head())

    # -----------------------------------
    # 2. PROCESSING TIME
    # -----------------------------------
    if applications is not None:
        applications['APPLICATION_DATE'] = pd.to_datetime(applications['APPLICATION_DATE'], errors='coerce')
        applications['APPROVAL_DATE'] = pd.to_datetime(applications.get('APPROVAL_DATE'), errors='coerce')

        if 'BRANCH_ID' in applications.columns:
            applications['PROCESSING_DAYS'] = (
                applications['APPROVAL_DATE'] - applications['APPLICATION_DATE']
            ).dt.days

            processing = applications.groupby('BRANCH_ID')['PROCESSING_DAYS'].mean()
            results['processing_time'] = processing

            print("\nProcessing Time:\n", processing.head())

    # -----------------------------------
    # 3. RECOVERY RATE
    # -----------------------------------
    if defaults is not None:
        defaults['RECOVERY_RATE'] = defaults['RECOVERY_AMOUNT'] / defaults['DEFAULT_AMOUNT']

        recovery = defaults.groupby('LOAN_ID')['RECOVERY_RATE'].mean()
        results['recovery_rate'] = recovery

        print("\nRecovery Rate:\n", recovery.head())

    # -----------------------------------
    # 4. REGION COMPARISON
    # -----------------------------------
    if 'REGION' in df.columns:
        region_perf = df.groupby('REGION').agg({
            'LOAN_AMOUNT': 'sum',
            'DEFAULT_FLAG': 'mean'
        }).rename(columns={
            'LOAN_AMOUNT': 'TOTAL_DISBURSEMENT',
            'DEFAULT_FLAG': 'DEFAULT_RATE'
        })

        results['region_performance'] = region_perf

        print("\nRegion Performance:\n", region_perf)

    return results