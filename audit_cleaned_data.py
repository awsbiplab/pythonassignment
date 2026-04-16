import pandas as pd
import os

def audit_cleaned_data():

    path = "data/cleaned"

    print("\n🔍 STARTING DATA AUDIT...\n")

    # Expected columns for validation
    expected_columns = {
        "customers": ["CUSTOMER_ID", "REGION"],
        "loans": ["LOAN_ID", "CUSTOMER_ID", "LOAN_AMOUNT", "INTEREST_RATE", "LOAN_TERM", "REGION"],
        "applications": ["LOAN_ID", "APPLICATION_DATE"],
        "transactions": ["LOAN_ID", "AMOUNT"],
        "defaults": ["LOAN_ID", "DEFAULT_AMOUNT"],
        "branches": ["REGION"]
    }

    # Loop through all cleaned files
    for file in os.listdir(path):

        if file.endswith(".csv"):

            name = file.replace(".csv", "")
            file_path = os.path.join(path, file)

            df = pd.read_csv(file_path)

            print(f"\n📁 DATASET: {name}")
            print("=" * 50)

            # -----------------------------------
            # BASIC INFO
            # -----------------------------------
            print(f"Shape: {df.shape}")
            print(f"Columns: {list(df.columns)}")

            # -----------------------------------
            # EMPTY CHECK
            # -----------------------------------
            if df.empty:
                print("❌ ERROR: Dataset is EMPTY")
                continue

            # -----------------------------------
            # EXPECTED COLUMN CHECK
            # -----------------------------------
            if name in expected_columns:
                for col in expected_columns[name]:
                    if col in df.columns:
                        print(f"✅ {col} present")
                    else:
                        print(f"❌ {col} MISSING")

            # -----------------------------------
            # KEY COLUMN CHECK
            # -----------------------------------
            if 'LOAN_ID' in df.columns:
                missing = df['LOAN_ID'].isna().sum()
                print(f"LOAN_ID missing values: {missing}")

            if 'CUSTOMER_ID' in df.columns:
                missing = df['CUSTOMER_ID'].isna().sum()
                print(f"CUSTOMER_ID missing values: {missing}")

            if 'REGION' in df.columns:
                missing = df['REGION'].isna().sum()
                print(f"REGION missing values: {missing}")

            # -----------------------------------
            # NUMERIC CHECK
            # -----------------------------------
            numeric_cols = df.select_dtypes(include='number').columns

            if len(numeric_cols) > 0:
                print("\nNumeric Summary:")
                print(df[numeric_cols].describe())

            # -----------------------------------
            # NULL SUMMARY
            # -----------------------------------
            print("\nMissing Values Summary:")
            print(df.isnull().sum())

            # -----------------------------------
            # SAMPLE DATA
            # -----------------------------------
            print("\nSample Data:")
            print(df.head())

    print("\n✅ DATA AUDIT COMPLETED\n")


# -----------------------------------
# RUN SCRIPT
# -----------------------------------
if __name__ == "__main__":
    audit_cleaned_data()