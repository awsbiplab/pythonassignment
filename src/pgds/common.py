import pandas as pd

class DataLoader:
    def load_all(self):
        return {
            "applications": pd.read_csv("data/applications.csv"),
            "customers": pd.read_csv("data/customers.csv"),
            "loans": pd.read_csv("data/loans.csv"),
            "defaults": pd.read_csv("data/defaults.csv"),
            "transactions": pd.read_csv("data/transactions.csv"),
            "branches": pd.read_csv("data/branches.csv"),
        }

class DataMerger:
    def merge(self, data):
        df = data["applications"]
        df = df.merge(data["customers"], on="Customer_ID", how="left")
        df = df.merge(data["loans"], on="Loan_ID", how="left")
        df = df.merge(data["defaults"], on="Loan_ID", how="left")
        return df
