import pandas as pd

customers = pd.DataFrame({
    'customer_id': [1, 2, 3, 4],
    'name': ['Alice', 'Bob', 'Charlie', 'Diana'],
    'city': ['Athens', 'Thessaloniki', 'Patras', 'Athens']
})

orders = pd.DataFrame({
    'order_id': [101, 102, 103, 104, 105],
    'customer_id': [1, 2, 2, 5, 1],
    'amount': [50, 200, 75, 300, 150]
})

# Creating 4 merges
inner_merged = customers.merge(orders, on='customer_id', how='inner') # Waiting 4 rows

left_merged = customers.merge(orders, on='customer_id', how='left') # Waiting 6 rows

right_merged = customers.merge(orders, on='customer_id', how='right') # Waiting 5 rows

outer_merged = customers.merge(orders, on='customer_id', how='outer') # Waiting 7 rows

print(outer_merged)