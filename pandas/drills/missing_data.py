import pandas as pd
import numpy as np

np.random.seed(42)

df = pd.DataFrame({
    'patient_id': range(1, 21),
    'age': [45, 52, np.nan, 61, 38, 47, 55, np.nan, 42, 68,
            33, 59, 71, np.nan, 48, 56, 39, 62, 51, 44],
    'gender': ['M','F','M','F','M','F','M','F','M','F',
               'M','F','M','F','M','F','M','F','M','F'],
    'bmi': [28.5, 31.2, 26.8, np.nan, 29.1, 33.5, np.nan, 27.9, 30.1, 32.8,
            25.4, np.nan, np.nan, 28.9, 31.5, np.nan, 26.2, np.nan, 29.7, 30.8],
    'a1c_result': [np.nan, 7.2, np.nan, 8.1, np.nan, 6.9, np.nan, 7.8, np.nan, 8.5,
                   np.nan, 7.1, 9.2, np.nan, np.nan, 7.6, np.nan, 8.9, np.nan, np.nan],
    'readmitted': [0, 1, 0, 1, 0, 1, 0, 1, 0, 1,
                   0, 1, 1, 0, 0, 1, 0, 1, 0, 0]
})

# Create a new df with 2 new features
missing_report = pd.DataFrame({
    'n_missing': df.isna().sum(),
    'pct_missing': df.isna().sum()/len(df),   
}).sort_values('pct_missing', ascending=False)


# df imputation
df['age'] = df['age'].fillna(df['age'].median())
df['bmi'] = df.groupby('gender')['bmi'].transform(lambda s: s.fillna(s.median()))
df['a1c_tested'] = df['a1c_result'].notna()
df['a1c_result_filled'] = df['a1c_result'].fillna(-1)


print(df.isna().sum())