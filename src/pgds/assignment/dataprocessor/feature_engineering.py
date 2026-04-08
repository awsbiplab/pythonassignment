
def create_features(data):
    loans = data['loans']
    defaults = data['defaults']
    loans['DEFAULT_FLAG'] = loans['LOAN_ID'].isin(defaults['LOAN_ID']).astype(int)
    data['loans'] = loans
    return data
