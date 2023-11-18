# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt

# Calculate skewness of loan_payments dataset
# Skewness is a measure of the asymmetry of the probability distribution
# of a real-valued random variable about its mean
loan_payments = pd.read_csv(r'C:\Users\Louis\Aicore\Dataset_loan_project\loan_payments.csv')
transformed_df = pd.read_csv(r'C:\Users\Louis\Aicore\Dataset_loan_project\transformed_df.csv')

skewness_loan_payments = loan_payments.skew(axis=0, skipna=True, numeric_only=True)

# Calculate skewness of transformed_data dataset
skewness_transformed_df= transformed_df.skew(axis=0, skipna=True, numeric_only=True)

# Print skewness of both datasets
print("Skewness of loan_payments:")
print(skewness_loan_payments)
print("\nSkewness of transformed_df:")
print(skewness_transformed_df)

# Create subplots for plotting
fig, ax = plt.subplots(2, 1, figsize=(10, 6))

# Plot skewness of loan_payments dataset
ax[0].bar(skewness_loan_payments.index, skewness_loan_payments.values)
ax[0].set_title('Skewness of loan_payments')
ax[0].tick_params(axis='x', rotation=90)  # Rotate x-axis labels for readability

# Plot skewness of transformed_data dataset
ax[1].bar(skewness_transformed_df.index, skewness_transformed_df.values)
ax[1].set_title('Skewness of transformed_df')
ax[1].tick_params(axis='x', rotation=90)  # Rotate x-axis labels for readability

# Adjust subplot params so that subplots fit into the figure area
plt.tight_layout()

# Display the figure
plt.show()
