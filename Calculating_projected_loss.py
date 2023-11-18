import pandas as pd

# Load your data into a DataFrame
df = pd.read_csv(r'C:\Users\Louis\Aicore\Dataset_loan_project\transformed_df.csv')  

# Calculate the expected revenue for each loan
df['expected_revenue'] = df['loan_amount'] * (1 + df['int_rate'] / 100) ** df['term']

# Calculate the actual revenue for each loan

df['actual_revenue'] = df['total_payment']

# Calculate the lost revenue for each loan
df['lost_revenue'] = df['expected_revenue'] - df['actual_revenue']

# Calculate the total percentage of expected revenue that was lost
total_expected_revenue = df['expected_revenue'].sum()
total_lost_revenue = df['lost_revenue'].sum()
percentage_lost = total_lost_revenue / total_expected_revenue * 100
print(f"Total percentage of expected revenue that was lost: {percentage_lost}%")

# Calculate the increase in revenue this would have been for the company
increase_in_revenue = total_expected_revenue - df['actual_revenue'].sum()
print(f"Increase in revenue this would have been for the company: {increase_in_revenue}")