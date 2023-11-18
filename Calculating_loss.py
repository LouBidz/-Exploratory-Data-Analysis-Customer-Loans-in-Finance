import pandas as pd

df = pd.read_csv(r'C:\Users\Louis\Aicore\Dataset_loan_project\transformed_df.csv')
# Assuming df is your DataFrame
charged_off_loans = df[df['loan_status'] == 'Charged Off']

# Calculate the percentage of charged off loans
percentage_charged_off = len(charged_off_loans) / len(df) * 100
print(f"Percentage of charged off loans: {percentage_charged_off}%")

# Calculate the amount paid towards these loans before being charged off
# Assuming 'total_payment' is the column that represents the total payment towards the loan
amount_paid = charged_off_loans['total_payment'].sum()
print(f"Total amount paid towards charged off loans: {amount_paid}")