SELECT * FROM job_openings_db.`ds_salaries (1)`;

# Provide a top 20 of the entry-level positions with the highest pay in the year 2022 

SELECT job_title, salary_in_usd FROM job_openings_db.`ds_salaries (1)`
WHERE experience_level = 'EN' AND work_year = 2022
ORDER BY salary_in_usd DESC
LIMIT 20;

# Calculate the average salary of a machine learning engineer 

SELECT AVG(salary) AS average_salary
FROM job_openings_db.`ds_salaries (1)`
WHERE job_title = 'Machine Learning Engineer' AND experience_level = 'MI';

# Select the job openings in Spain that are not 'experienced level' (EX) and provide the first 20 positions, order by job title 

SELECT salary, job_title, experience_level, company_size FROM job_openings_db.`ds_salaries (1)`
WHERE company_location = 'ES' AND experience_level !='EX'
ORDER BY job_title ASC
LIMIT 20;