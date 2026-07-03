SELECT
name, 
department,
salary,
AVG(salary) OVER (PARTITION BY department) AS dept_avg,
salary-AVG(salary) OVER (PARTITION BY department) AS diff_from_avg,
LAG(salary) OVER (PARTITION BY department ORDER BY hire_date ASC) AS prev_hired_salary
FROM employees;