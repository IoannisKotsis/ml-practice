import pandas as pd

df = pd.DataFrame({
    'date': pd.to_datetime([
        '2024-01-01', '2024-01-02', '2024-01-03', '2024-01-04', '2024-01-05',
        '2024-01-01', '2024-01-02', '2024-01-03', '2024-01-04', '2024-01-05'
    ]),
    'customer_id': ['A','A','A','A','A','B','B','B','B','B'],
    'amount': [100, 120, 90, 150, 130, 200, 180, 220, 210, 250]
})

# Inserting 2 new rows
df['prev_amount'] = df.groupby('customer_id')['amount'].shift(1)
df['pct_change'] = ((df['amount']-df['prev_amount'])/df['prev_amount']) * 100 # or better: df.groupby('customer_id')['amount'].pct_change() * 100

print(df)
