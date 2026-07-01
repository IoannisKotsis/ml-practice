import pandas as pd
import numpy as np

np.random.seed(42)
df = pd.DataFrame({
    'date': pd.to_datetime(
        ['2024-01-01','2024-01-15','2024-02-01','2024-02-20','2024-03-05','2024-03-25','2024-04-10','2024-04-28'] * 3
    ),
    'hospital_id': ['H1']*8 + ['H2']*8 + ['H3']*8,
    'amount': np.random.randint(1000, 10000, size=24)
})
df = df.sort_values(['hospital_id', 'date']).reset_index(drop=True)

# Creating 3 new features
df['prev_amount'] = df.groupby('hospital_id')['amount'].shift(1)
df['avg_last_3_excl_current'] = df.groupby('hospital_id')['amount'].transform(lambda x: x.shift(1).rolling(3).mean())
df['amount_vs_history'] = df['amount'] / df['avg_last_3_excl_current']

print(df)