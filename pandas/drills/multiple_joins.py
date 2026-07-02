import pandas as pd
import numpy as np

hospitals = pd.DataFrame({
    'hospital_id': ['H1', 'H2', 'H3', 'H4', 'H5'],
    'name': ['General Athens', 'Metropolitan', 'Thessaloniki Central', 'Patras Uni', 'Heraklion'],
    'region_code': ['ATT', 'ATT', 'MAK', 'PEL', 'CRE'],
    'beds': [500, 300, 450, 250, 200]
})

orders = pd.DataFrame({
    'order_id': range(1001, 1013),
    'hospital_id': ['H1','H1','H1','H2','H2','H3','H3','H3','H3','H4','H6','H6'],
    'amount': [5000, 3000, 7000, 2000, 4500, 8000, 1500, 3500, 2500, 6000, 1000, 2000]
})

regions = pd.DataFrame({
    'region_code': ['ATT', 'MAK', 'PEL', 'CRE', 'THE'],
    'region_name': ['Attica', 'Macedonia', 'Peloponnese', 'Crete', 'Thessaly'],
    'population_millions': [3.8, 1.9, 1.1, 0.6, 0.7]
})

orders_summary = orders.groupby('hospital_id').agg(      
    total_orders=('order_id', 'count'),
    total_revenue=('amount', 'sum'),
    avg_order_value=('amount', 'mean')
).reset_index()

new_df = pd.merge(hospitals,
                  orders_summary,
                  on='hospital_id',
                  how='left')

new_df['total_orders'] = new_df['total_orders'].fillna(0).astype(int)

new_df = pd.merge(new_df,
                  regions,
             on='region_code',
             how='left')

new_df = new_df.drop(columns='region_code')


print(new_df)