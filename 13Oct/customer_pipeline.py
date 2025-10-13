import pandas as pd
from datetime import datetime

# Step 1: Extract data from customers.csv
input_file = 'customers.csv'
df = pd.read_csv(input_file)

# Step 2: Transform data
def categorize_age(age):
    if age < 30:
        return "Young"
    elif 30 <= age < 50:
        return "Adult"
    else:
        return "Senior"

# Add AgeGroup column
df['AgeGroup'] = df['Age'].apply(categorize_age)

# Filter out customers younger than 20
df_filtered = df[df['Age'] >= 20]

# Step 3: Load transformed data into filtered_customers.csv
output_file = 'filtered_customers.csv'
df_filtered.to_csv(output_file, index=False)

# Step 4: Print the time the pipeline was executed
execution_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
