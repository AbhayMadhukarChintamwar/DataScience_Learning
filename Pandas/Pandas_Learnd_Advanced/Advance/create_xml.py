import pandas as pd
import numpy as np

# Number of records
n = 12000  # 10k+ data

# Set random seed for reproducibility
np.random.seed(42)

# Sample data pools
it_roles = ['Software Engineer', 'Data Scientist', 'DevOps Engineer', 'Backend Developer', 'Frontend Developer']
finance_roles = ['Accountant', 'Financial Analyst', 'Investment Banker', 'Auditor', 'Risk Manager']

# companies = ['TCS', 'Infosys', 'Wipro', 'HDFC', 'ICICI', 'Deloitte', 'Accenture']
companies = ['TCS', 'Infosys', 'Wipro', 'Microsoft ','Deloitte', 'Accenture','Google','Amazon']
cities = ['Mumbai', 'Pune', 'Hyderabad', 'Bangalore', 'Delhi']

# Generate dataset
data = {
    'Employee_ID': np.arange(1, n + 1),
    'Name': ['Employee_' + str(i) for i in range(1, n + 1)],
    'Department': np.random.choice(['IT', 'Finance'], n),
    'Role': [
        np.random.choice(it_roles) if dept == 'IT' else np.random.choice(finance_roles)
        for dept in np.random.choice(['IT', 'Finance'], n)
    ],
    'Company': np.random.choice(companies, n),
    'City': np.random.choice(cities, n),
    'Salary': np.random.randint(300000, 2000000, n),
    'Experience_Years': np.round(np.random.uniform(0.5, 15, n), 1)
}

# Create DataFrame
df = pd.DataFrame(data)

# Export to XML
file_path = "it_finance_data.xml"
df.to_xml(file_path, root_name='Employees', row_name='Employee', index=False)

print(f"XML file created successfully: {file_path}")