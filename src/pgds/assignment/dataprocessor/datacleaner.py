import pandas as pd
def cleanData(data):
    # Customers
    data['customers'] = data['customers'].drop_duplicates()

    # Loans
    loans = data['loans']
    loans = loans.dropna(subset=['Customer_ID'])
    loans = loans[loans['Loan_Amount'] > 0]
    data['loans'] = loans

    # Applications
    data['applications']['Application_Date'] = pd.to_datetime(
        data['applications']['Application_Date'], errors='coerce'
    )

    return data