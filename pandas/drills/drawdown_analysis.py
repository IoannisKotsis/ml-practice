import pandas as pd
import numpy as np

np.random.seed(42)
dates = pd.date_range('2024-01-01', periods=30, freq='D')
prices_A = 100 + np.cumsum(np.random.randn(30) * 2)
prices_B = 100 + np.cumsum(np.random.randn(30) * 3)

df = pd.DataFrame({
    'date': list(dates) * 2,
    'ticker': ['STOCK_A']*30 + ['STOCK_B']*30,
    'price': list(prices_A) + list(prices_B)
})
df = df.sort_values(['ticker', 'date']).reset_index(drop=True)

# Creating 4 new features-columns
df['all_time_high'] = df.groupby('ticker')['price'].cummax()
df['drawdown_pct'] = ((df['price'] - df['all_time_high'])/df['all_time_high']) * 100
df['max_drawdown_to_date'] = df.groupby('ticker')['drawdown_pct'].cummin()
df['is_at_peak'] = df['price'] == df['all_time_high']

print(df)