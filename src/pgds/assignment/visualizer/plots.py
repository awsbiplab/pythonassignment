
import matplotlib.pyplot as plt
import seaborn as sns

def plot_all(df):
    df['LOAN_AMOUNT'].hist()
    plt.savefig("reports/figures/loan_dist.png")
    plt.clf()

    df.groupby('REGION')['DEFAULT_FLAG'].mean().plot(kind='bar')
    plt.savefig("reports/figures/default_region.png")
    plt.clf()

    sns.heatmap(df.corr(numeric_only=True))
    plt.savefig("reports/figures/corr.png")
    plt.clf()

def plot_descriptive(df, applications=None):

    # -----------------------------
    # 1. DISTRIBUTIONS
    # -----------------------------
    df['LOAN_AMOUNT'].hist()
    plt.title("Loan Amount Distribution")
    plt.savefig("reports/figures/loan_distribution.png")
    plt.clf()

    if 'EMI_AMOUNT' in df.columns:
        df['EMI_AMOUNT'].hist()
        plt.title("EMI Distribution")
        plt.savefig("reports/figures/emi_distribution.png")
        plt.clf()

    df['CREDIT_SCORE'].hist()
    plt.title("Credit Score Distribution")
    plt.savefig("reports/figures/credit_score_distribution.png")
    plt.clf()

    # -----------------------------
    # 2. REGIONAL TRENDS
    # -----------------------------
    if 'REGION' in df.columns:
        df.groupby('REGION')['LOAN_AMOUNT'].sum().plot(kind='bar')
        plt.title("Loan Disbursement by Region")
        plt.savefig("reports/figures/region_disbursement.png")
        plt.clf()

        df.groupby('REGION')['DEFAULT_FLAG'].mean().plot(kind='bar')
        plt.title("Default Rate by Region")
        plt.savefig("reports/figures/region_default.png")
        plt.clf()

    # -----------------------------
    # 3. MONTHLY TRENDS
    # -----------------------------
    if applications is not None:
        applications['APPLICATION_DATE'] = pd.to_datetime(applications['APPLICATION_DATE'])

        applications.groupby(
            applications['APPLICATION_DATE'].dt.to_period('M')
        ).size().plot()

        plt.title("Monthly Loan Applications")
        plt.savefig("reports/figures/monthly_applications.png")
        plt.clf()

import seaborn as sns
import matplotlib.pyplot as plt

def plot_default_risk(df):

    # -----------------------------------
    # 1. LOAN ATTRIBUTE CORRELATION
    # -----------------------------------
    cols = ['LOAN_AMOUNT', 'INTEREST_RATE', 'CREDIT_SCORE', 'DEFAULT_FLAG']
    cols = [c for c in cols if c in df.columns]

    if len(cols) >= 2:
        sns.heatmap(df[cols].corr(), annot=True)
        plt.title("Loan Attribute Correlation")
        plt.savefig("reports/figures/loan_correlation.png")
        plt.clf()

    # -----------------------------------
    # 2. PAIRWISE HEATMAP
    # -----------------------------------
    pair_cols = ['EMI_AMOUNT', 'OVERDUE_AMOUNT', 'DEFAULT_AMOUNT']
    pair_cols = [c for c in pair_cols if c in df.columns]

    if len(pair_cols) >= 2:
        sns.heatmap(df[pair_cols].corr(), annot=True)
        plt.title("Pairwise Correlation Heatmap")
        plt.savefig("reports/figures/pairwise_heatmap.png")
        plt.clf()

# task 4

def plot_branch_performance(df):

    # -----------------------------
    # 1. DISBURSEMENT BY REGION
    # -----------------------------
    if 'REGION' in df.columns:
        df.groupby('REGION')['LOAN_AMOUNT'].sum().plot(kind='bar')
        plt.title("Loan Disbursement by Region")
        plt.savefig("reports/figures/branch_region_disbursement.png")
        plt.clf()

    # -----------------------------
    # 2. DEFAULT RATE BY REGION
    # -----------------------------
    if 'REGION' in df.columns:
        df.groupby('REGION')['DEFAULT_FLAG'].mean().plot(kind='bar')
        plt.title("Default Rate by Region")
        plt.savefig("reports/figures/branch_region_default.png")
        plt.clf()

# task 5
import matplotlib.pyplot as plt

def plot_customer_segments(df):

    # -----------------------------------
    # CREDIT SEGMENT DISTRIBUTION
    # -----------------------------------
    df['CREDIT_SEGMENT'].value_counts().plot(kind='bar')
    plt.title("Customer Distribution by Credit Segment")
    plt.savefig("reports/figures/customer_credit_segment.png")
    plt.clf()

    # -----------------------------------
    # DEFAULT RATE BY SEGMENT
    # -----------------------------------
    df.groupby('CREDIT_SEGMENT')['DEFAULT_FLAG'].mean().plot(kind='bar')
    plt.title("Default Rate by Credit Segment")
    plt.savefig("reports/figures/customer_default_segment.png")
    plt.clf()

# task 6

def plot_statistical_analysis(df, defaults=None):

    # -----------------------------------
    # DEFAULT RISK HEATMAP
    # -----------------------------------
    cols = ['CREDIT_SCORE', 'LOAN_AMOUNT', 'INTEREST_RATE', 'DEFAULT_FLAG']
    cols = [c for c in cols if c in df.columns]

    if len(cols) >= 2:
        sns.heatmap(df[cols].corr(), annot=True)
        plt.title("Default Risk Correlation")
        plt.savefig("reports/figures/default_risk_heatmap.png")
        plt.clf()

    # -----------------------------------
    # ADVANCED PAIRWISE HEATMAP
    # -----------------------------------
    if defaults is not None:
        defaults['RECOVERY_RATE'] = defaults['RECOVERY_AMOUNT'] / defaults['DEFAULT_AMOUNT']
        merged = df.merge(defaults, on='LOAN_ID', how='left')

        pair_cols = ['EMI_AMOUNT', 'RECOVERY_RATE', 'DEFAULT_AMOUNT']
        pair_cols = [c for c in pair_cols if c in merged.columns]

        if len(pair_cols) >= 2:
            sns.heatmap(merged[pair_cols].corr(), annot=True)
            plt.title("Advanced Pairwise Correlation")
            plt.savefig("reports/figures/advanced_heatmap.png")
            plt.clf()

# Task 7

def plot_transaction_recovery(df, transactions, defaults):

    # -----------------------------
    # PENALTY DISTRIBUTION
    # -----------------------------
    if 'TRANSACTION_TYPE' in transactions.columns:
        transactions['TRANSACTION_TYPE'].value_counts().plot(kind='bar')
        plt.title("Transaction Type Distribution")
        plt.savefig("reports/figures/transaction_types.png")
        plt.clf()

    # -----------------------------
    # RECOVERY RATE DISTRIBUTION
    # -----------------------------
    if 'RECOVERY_AMOUNT' in defaults.columns:
        defaults['RECOVERY_RATE'] = defaults['RECOVERY_AMOUNT'] / defaults['DEFAULT_AMOUNT']

        defaults['RECOVERY_RATE'].hist()
        plt.title("Recovery Rate Distribution")
        plt.savefig("reports/figures/recovery_distribution.png")
        plt.clf()

# Task 8

def plot_emi_analysis(df):

    # -----------------------------
    # EMI vs DEFAULT
    # -----------------------------
    if 'EMI_AMOUNT' in df.columns:
        df.groupby('EMI_AMOUNT')['DEFAULT_FLAG'].mean().plot()
        plt.title("EMI vs Default Probability")
        plt.savefig("reports/figures/emi_default.png")
        plt.clf()

    # -----------------------------
    # EMI BUCKET ANALYSIS
    # -----------------------------
    if 'EMI_AMOUNT' in df.columns:
        df['EMI_BUCKET'] = pd.qcut(df['EMI_AMOUNT'], q=5, duplicates='drop')
        df.groupby('EMI_BUCKET')['DEFAULT_FLAG'].mean().plot(kind='bar')
        plt.title("Default Rate by EMI Bucket")
        plt.savefig("reports/figures/emi_bucket.png")
        plt.clf()

    # -----------------------------
    # EMI BY LOAN TYPE
    # -----------------------------
    if 'LOAN_TYPE' in df.columns:
        df.groupby('LOAN_TYPE')['EMI_AMOUNT'].mean().plot(kind='bar')
        plt.title("EMI by Loan Type")
        plt.savefig("reports/figures/emi_loan_type.png")
        plt.clf()