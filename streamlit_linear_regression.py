import streamlit as st
import pandas as pd
import pickle
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# Assuming you have already loaded and processed the dataset into X_encoded and y
# X_encoded = ...
# y = ...

# Splitting the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X_encoded, y, test_size=0.2, random_state=42)

# Training the Linear Regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Save the trained model using pickle
with open("trained_linear_regression_model.pkl", "wb") as file:
    pickle.dump(model, file)

def load_model():
    # Load the trained regression model from the file
    with open("trained_linear_regression_model.pkl", "rb") as file:
        model = pickle.load(file)
    return model

def preprocess_user_input(user_input, X_encoded_columns):
    # Create a DataFrame with the same columns as X_encoded and fill it with zeros
    encoded_user_input = pd.DataFrame(0, index=user_input.index, columns=X_encoded_columns)

    # Update the columns with user input values (assuming user_input is a DataFrame)
    encoded_user_input.update(user_input)

    return encoded_user_input

def predict_salary(model, user_input):
    # Load the column names used for one-hot encoding during training
    # Assuming X_encoded was created in the same way as during training
    X_encoded_columns = X_encoded.columns.tolist()

    # Preprocess the user input to match the format used during model training
    encoded_user_input = preprocess_user_input(user_input, X_encoded_columns)

    # Make the salary prediction based on preprocessed user input
    predicted_salary = model.predict(encoded_user_input)
    return predicted_salary[0]

def main():
    st.title("Salary Estimator")
    
    experience_level = st.selectbox("Select Experience Level", ['SE','MI','EN','EX'])
    employment_type = st.selectbox("Select Employment Type", ['FT','CT','FL','PT'])
    
    job_title = st.selectbox("Enter Job Title", ['Principal Data Scientist', 'ML Engineer', 'Data Scientist', 'Applied Scientist', 
                                                 'Data Analyst', 'Data Modeler', 'Research Engineer', 'Analytics Engineer', 
                                                 'Business Intelligence Engineer', 'Machine Learning Engineer', 'Data Strategist', 
                                                 'Data Engineer', 'Computer Vision Engineer', 'Data Quality Analyst', 'Compliance Data Analyst', 
                                                 'Data Architect', 'Applied Machine Learning Engineer', 'AI Developer', 'Research Scientist', 
                                                 'Data Analytics Manager', 'Business Data Analyst', 'Applied Data Scientist', 'Staff Data Analyst', 
                                                 'ETL Engineer', 'Data DevOps Engineer', 'Head of Data', 'Data Science Manager', 'Data Manager', 
                                                 'Machine Learning Researcher', 'Big Data Engineer', 'Data Specialist', 'Lead Data Analyst', 
                                                 'BI Data Engineer', 'Director of Data Science', 'Machine Learning Scientist', 'MLOps Engineer', 
                                                 'AI Scientist', 'Autonomous Vehicle Technician', 'Applied Machine Learning Scientist',
                                                 'Lead Data Scientist', 'Cloud Database Engineer', 'Financial Data Analyst', 'Data Infrastructure Engineer',
                                                 'Software Data Engineer', 'AI Programmer', 'Data Operations Engineer', 'BI Developer', 'Data Science Lead', 
                                                 'Deep Learning Researcher', 'BI Analyst', 'Data Science Consultant', 'Data Analytics Specialist', 
                                                 'Machine Learning Infrastructure Engineer', 'BI Data Analyst', 'Head of Data Science', 'Insight Analyst', 
                                                 'Deep Learning Engineer', 'Machine Learning Software Engineer', 'Big Data Architect', 'Product Data Analyst', 
                                                 'Computer Vision Software Engineer', 'Azure Data Engineer', 'Marketing Data Engineer', 'Data Analytics Lead', 
                                                 'Data Lead', 'Data Science Engineer', 'Machine Learning Research Engineer', 'NLP Engineer', 'Manager Data Management', 
                                                 'Machine Learning Developer', '3D Computer Vision Researcher', 'Principal Machine Learning Engineer', 
                                                 'Data Analytics Engineer', 'Data Analytics Consultant', 'Data Management Specialist', 'Data Science Tech Lead', 
                                                 'Data Scientist Lead', 'Cloud Data Engineer', 'Data Operations Analyst', 'Marketing Data Analyst', 'Power BI Developer', 
                                                 'Product Data Scientist', 'Principal Data Architect', 'Machine Learning Manager', 'Lead Machine Learning Engineer', 
                                                 'ETL Developer', 'Cloud Data Architect', 'Lead Data Engineer', 'Head of Machine Learning', 'Principal Data Analyst', 
                                                 'Principal Data Engineer', 'Staff Data Scientist', 'Finance Data Analyst'])
    
    company_location = st.selectbox("Company Location", 
                                     ['ES', 'US', 'CA', 'DE', 'GB', 'NG', 'IN', 'HK', 'NL', 'CH',
                                      'CF', 'FR', 'FI', 'UA', 'IE', 'IL', 'GH', 'CO', 'SG', 'AU',
                                      'SE', 'SI', 'MX', 'BR', 'PT', 'RU', 'TH', 'HR', 'VN', 'EE',
                                      'AM', 'BA', 'KE', 'GR', 'MK', 'LV', 'RO', 'PK', 'IT', 'MA',
                                      'PL', 'AL', 'AR', 'LT', 'AS', 'CR', 'IR', 'BS', 'HU', 'AT',
                                      'SK', 'CZ', 'TR', 'PR', 'DK', 'BO', 'PH', 'BE', 'ID', 'EG',
                                      'AE', 'LU', 'MY', 'HN', 'JP', 'DZ', 'IQ', 'CN', 'NZ', 'CL',
                                      'MD', 'MT'])

    remote_ratio = st.slider("Remote Work Ratio (%)", min_value=0, max_value=100, value=50, step=50)

    user_input = pd.DataFrame({
        'experience_level': [experience_level],
        'employment_type': [employment_type],
        'company_location': [company_location],
        'remote_ratio': [remote_ratio]
    })

    # Load the trained regression model
    model = load_model()

    # Check if the user has provided all the inputs
    if st.button("Estimate Salary"):
        if company_size > 0:
            # Make the salary prediction based on user input
            predicted_salary = predict_salary(model, user_input)
            st.write(f"Estimated Salary: ${predicted_salary:.2f}")
        else:
            st.warning("Please provide a valid company size.")

if __name__ == "__main__":
    main()