# Task 1a
SELECT name,
department,
salary,
RANK() OVER (PARTITION BY department ORDER BY salary DESC) AS salary_rank_in_dept
FROM employees
ORDER BY department, salary_rank_in_dept;

# Task 1b
WITH ranked AS (
    SELECT name, salary, department, ROW_NUMBER() OVER (PARTITION BY department ORDER BY salary DESC, hire_date ASC) AS rn
    FROM employees
)
SELECT * FROM ranked WHERE rn = 1;

# Task 1c
