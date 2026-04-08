import pandas as pd

def loadData():
    customers = pd.read_csv("data/customers.csv")
    applications = pd.read_csv("data/applications.csv")
    loans = pd.read_csv("data/loans.csv")
    defaults = pd.read_csv("data/defaults.csv")
    transactions = pd.read_csv("data/transactions.csv")
    branches = pd.read_csv("data/branches.csv")
    return customers, applications, loans, defaults, transactions, branches

def checkMissingValues(dfs):
    for df in dfs:
        print(df)
        print(df.isnull().sum())

