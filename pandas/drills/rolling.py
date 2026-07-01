import pandas as pd

df = pd.DataFrame({
    'date': pd.to_datetime([
        '2024-01-01', '2024-01-02', '2024-01-03', '2024-01-04', '2024-01-05', '2024-01-06',
        '2024-01-01', '2024-01-02', '2024-01-03', '2024-01-04', '2024-01-05', '2024-01-06'
    ]),
    'customer_id': ['A','A','A','A','A','A','B','B','B','B','B','B'],
    'amount': [100, 120, 90, 150, 130, 170, 200, 180, 220, 210, 250, 240]
})

# Insert 2 new rows
df['rolling_avg_3'] = df.groupby('customer_id')['amount'].rolling(3).mean().reset_index(level=0, drop=True)
"""
    df['rolling_avg_3'] = df.groupby('customer_id')['amount'].transform(lambda x: x.rolling(3).mean())
"""
    
df['is_above_avg'] = df['amount'] > df['rolling_avg_3']

print(df)