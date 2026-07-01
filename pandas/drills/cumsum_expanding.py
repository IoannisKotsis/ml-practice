import pandas as pd
import numpy as np

np.random.seed(0)
df = pd.DataFrame({
    'date': pd.date_range('2024-01-01', periods=10, freq='D').tolist() * 2,
    'hospital_id': ['H1']*10 + ['H2']*10,
    'daily_revenue': np.random.randint(500, 3000, size=20)
})
df = df.sort_values(['hospital_id', 'date']).reset_index(drop=True)

# Creating 3 new columns
df['cumulative_revenue'] = df.groupby('hospital_id')['daily_revenue'].cumsum()
df['avg_revenue_to_date'] = df.groupby('hospital_id')['daily_revenue'].transform(lambda x: x.expanding().mean())
df['is_best_day_so_far'] = df['daily_revenue'] == df.groupby('hospital_id')['daily_revenue'].cummax()

print(df)