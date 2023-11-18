import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r'C:\Users\Louis\Aicore\Dataset_loan_project\transformed_df.csv')

# Assuming df is your DataFrame
df['recovery_percentage_investor'] = df['total_payment'] / df['out_prncp_inv'] * 100
df['recovery_percentage_total'] = df['total_payment'] / df['loan_amount'] * 100

# Print the average recovery percentages
print("Average recovery percentage against investor funding:", df['recovery_percentage_investor'].mean())
print("Average recovery percentage against total funded:", df['recovery_percentage_total'].mean())

# Project recovery percentages 6 months into the future (this would depend on your specific projection model)
# For simplicity, let's assume a linear projection based on the past 6 months
df['projected_recovery_percentage'] = df['recovery_percentage_investor'] + (df['recovery_percentage_investor'].diff(periods=6) / 6 * 6)

# Visualize the data
df[['recovery_percentage_investor', 'projected_recovery_percentage']].plot()
