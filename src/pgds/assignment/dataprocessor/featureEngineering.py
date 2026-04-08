def createFeatures(data):
    loans = data['loans']
    defaults = data['defaults']

    loans['Default_Flag'] = loans['Loan_ID'].isin(defaults['Loan_ID']).astype(int)

    # Interest Income
    loans['Interest_Income'] = loans['Loan_Amount'] * loans['Interest_Rate']

    data['loans'] = loans
    return data