# CTE task
WITH order_counts AS (
    SELECT employee_id ,COUNT(*) AS total_orders
    FROM orders
    GROUP BY employee_id
)
SELECT name, department, total_orders
FROM employees e
JOIN order_counts oc ON oc.employee_id = e.employee_id
WHERE total_orders > 2;



# Multi-CTE task
WITH order_stats AS (
    SELECT employee_id,
    COUNT(*) AS total_orders,
    SUM(amount) AS total_revenue,
    AVG(amount) AS avg_order_value
    FROM orders
    GROUP BY employee_id
),
employee_info AS (
    SELECT e.name, e.department, e.salary,
    COALESCE(os.total_orders, 0) AS total_orders,
    COALESCE(os.total_revenue, 0) AS total_revenue,
    os.avg_order_value
    FROM employees e
    LEFT JOIN order_stats os ON e.employee_id = os.employee_id
),
with_dept_avg AS (
    SELECT *,
        AVG(total_revenue) OVER (PARTITION BY department) AS dept_avg_revenue,
        total_revenue > AVG(total_revenue) OVER (PARTITION BY department) AS is_above_dept_avg
    FROM employee_info
)
SELECT * FROM with_dept_avg;