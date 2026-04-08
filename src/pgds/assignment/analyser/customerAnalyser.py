import pandas as pd
def segment_customers(df):
    df['Segment'] = pd.cut(
        df['Credit_Score'],
        bins=[0, 500, 650, 750, 900],
        labels=['High Risk', 'Medium', 'Good', 'Excellent']
    )
    return df[['Customer_ID', 'Segment']]