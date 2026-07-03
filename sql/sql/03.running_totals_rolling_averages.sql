SELECT
name,
department,
hire_date,
salary,
SUM(salary) OVER (PARTITION BY department ORDER BY hire_date) AS cumulative_dept_payroll,
AVG (salary) OVER (PARTITION BY department ORDER BY hire_date ROWS BETWEEN 2 PRECEDING AND CURRENT ROW) AS rolling_avg_last_3
FROM employees;