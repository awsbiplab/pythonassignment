
def merge_all(data):
    df = data['loans'].merge(data['customers'], on='CUSTOMER_ID', how='left')
    if 'BRANCH_ID' in data['loans'].columns:
        df = df.merge(data['branches'], on='BRANCH_ID', how='left')
    return df
