# ironhack final version
FINAL VERSION OF THE PROJECT WITH ALL THE FILES 

The intention of this project is to provide a thorough analysis of a dataset regarding it-related job offerings, where we analyze relevant aspects such as the job title, location and gross average salary.

# METHODOLOGY

the project consists of an analysis of IT industry job openings from a kaggle datasets that has a sample size of 3,755 elements
we provide information on the gross salary, irrespective of other benefits (contributions to pensions schema, health insurance, travel allowances, etc.)
we do not take into account the inflation effect / consumer price index 
this dataset provides information as of April 2023, for updated information we might have to refer to a dataset that contains the most recent job openings 

# STREAMLIT UI 

In simple words, we are going to deploy a Streamlit user interface where we select the values for the input variables of our model ('experience_level','employment_type','job_title', 'remote_ratio') and the user eventually gets an estimate of the average salary (expressed in usd, irrespective of the job location) on how much he is going to get paid on average. Note that this is just an estimate which does not consider other aspects from the package benetis, such as travel allowance, insurance, overtime payment, etc. 

URL to the application deployed:
https://job-market-analysis.streamlit.app/

Github repository:
https://github.com/carlosruiz-stack/streamlit_app

# MAIN DATA SOURCE

Source to the Kaggle dataset: https://www.kaggle.com/datasets/arnabchaki/data-science-salaries-2023 

# KEY FINDINGS AND DATA VISUALISATION 

Summary of key findings: https://docs.google.com/document/d/1eYKkVRIIXONoLZCa148F_T_myIjpHlaAn3hx7pcCRqQ/edit?usp=sharing 

# ADDITIONAL CONSIDERATIONS 

Note: before we get into the project, we would like to highlight that we have also created another jupyter notebook where we perform the entire machine learning after removing outliers, following the iqr method. File is available in the following link: 

https://github.com/carlosruiz-stack/ironhack_final_version/blob/600f7441f4b314ed7409ccefd8cee210c6bfc965/it_job_offerings_removed_outliers.ipynb 

