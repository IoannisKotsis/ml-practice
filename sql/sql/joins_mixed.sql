WITH employees_stats AS(
    SELECT
    e.name,
    e.department,
    COUNT(*) AS total_orders,
    SUM(o.amount) AS total_revenue
    FROM employees e INNER JOIN orders o ON e.employee_id=o.employee_id
    GROUP BY e.employee_id, e.name, e.department
)
SELECT
    name,
    total_orders,
    department,
    RANK() OVER (PARTITION BY department ORDER BY total_revenue DESC) AS revenue_rank_in_dept,
    ROUND((total_revenue * 100.0 / SUM(total_revenue) OVER (PARTITION BY department))::numeric, 1) AS pct_of_dept_revenue
    FROM employees_stats
    ORDER BY revenue_rank_in_dept ASC, department ASC;
