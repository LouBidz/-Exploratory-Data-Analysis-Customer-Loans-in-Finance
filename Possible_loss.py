import pandas as pd

df = pd.read_csv(r'C:\Users\Louis\Aicore\Dataset_loan_project\transformed_df.csv')
# Step 1: Filter the data
behind_loans = df[df['loan_status'] == 'delinq_2yr'] # i also tried loan_status

# Step 2: Calculate the expected revenue for each loan
behind_loans['expected_revenue'] = behind_loans['loan_amount'] * (behind_loans['int_rate'] / 12) * behind_loans['term']

# Step 3: Sum the expected revenue
total_expected_revenue_behind = behind_loans['expected_revenue'].sum()

# Calculate the expected revenue for all loans
df['expected_revenue'] = df['loan_amount'] * (df['int_rate'] / 12) * df['term']
total_expected_revenue_all = df['expected_revenue'].sum()

# Step 4: Calculate the percentage loss
percentage_loss_behind = (total_expected_revenue_behind / total_expected_revenue_all) * 100

# Assuming 'charged_off_loans' is the DataFrame containing loans that are "Charged Off"
total_expected_revenue_charged_off = df['loan_status'].count()

# Calculate the total expected revenue from both categories
total_expected_revenue_default_behind = total_expected_revenue_charged_off + total_expected_revenue_behind

# Calculate the percentage of total revenue
percentage_total_revenue = (total_expected_revenue_default_behind / total_expected_revenue_all) * 100

# Print the total expected revenue from loans currently behind
print("Total expected revenue from loans currently behind: ", total_expected_revenue_behind)

# Print the percentage loss if these loans were to be "Charged Off"
print("Percentage loss if these loans were to be 'Charged Off': ", percentage_loss_behind)

# Print the total expected revenue from both categories
print("Total expected revenue from both categories: ", total_expected_revenue_default_behind)

# Print the percentage of total revenue represented by these customers
print("Percentage of total revenue represented by these customers: ", percentage_total_revenue)
