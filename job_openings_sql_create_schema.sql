use job_openings_db;

CREATE TABLE JOB_OPENING (
  job_opening_id INT PRIMARY KEY,
  job_title VARCHAR(255),
  salary DECIMAL(10, 2),
  location VARCHAR(255),
  currency VARCHAR(255),
  experience_level VARCHAR(255),
  employment_type VARCHAR(255)
);

CREATE TABLE COUNTRY (
  country_id INT PRIMARY KEY,
  country_name VARCHAR(255)
);

CREATE TABLE CURRENCY (
  currency_id INT PRIMARY KEY,
  currency_name VARCHAR(255)
);
