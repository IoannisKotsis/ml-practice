WITH top_employees AS (
    SELECT
    name,
    department,
    salary,
    ROW_NUMBER() OVER (PARTITION BY department ORDER BY salary DESC, hire_date ASC) AS rank_in_dept
    FROM employees
)
SELECT name, department, salary, rank_in_dept FROM top_employees
WHERE rank_in_dept in (1,2)
ORDER BY department, rank_in_dept;