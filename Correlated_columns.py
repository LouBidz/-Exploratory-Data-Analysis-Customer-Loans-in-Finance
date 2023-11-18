import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset

df = pd.read_csv(r'C:\Users\Louis\Aicore\Dataset_loan_project\transformed_df.csv')

# Step 1: Compute the correlation matrix
corr_matrix = df.corr()

# Visualise the correlation matrix
plt.figure(figsize=(10, 8))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')
plt.show()

# Step 2: Identify highly correlated columns
# Let's choose 0.75 as the correlation threshold
correlation_threshold = 1.00 # I chose 1 for this but you can move it up or down
highly_correlated = {}

for column in corr_matrix.columns:
    for index in corr_matrix.index:
        if abs(corr_matrix.loc[index, column]) > correlation_threshold and index != column:
            highly_correlated[(index, column)] = corr_matrix.loc[index, column]

print("Highly correlated columns:", highly_correlated)

# Step 3: Decide which columns to remove
# We'll remove the second column in each pair
columns_to_remove = set(column[0] for column in highly_correlated.keys())

print("Columns to remove:", columns_to_remove)

# Step 4: Remove the highly correlated columns from the dataset
df = df.drop(columns=columns_to_remove)

print("Dataset after removing highly correlated columns:")
print(df.head(5))