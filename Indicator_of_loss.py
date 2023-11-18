import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder

df = pd.read_csv('/content/transformed_data.csv')

# Step 1: Convert to numerical
label_encoder = LabelEncoder()
df['grade'] = label_encoder.fit_transform(df['grade'])
df['purpose'] = label_encoder.fit_transform(df['purpose'])
df['dti'] = label_encoder.fit_transform(df['dti'])

# Step 2: Filter the data
charged_off_loans = df[df['loan_status'] == 'Charged Off']
behind_loans = df[df['loan_status'] == 'Behind']

# Step 3: Visualize the data
plt.figure(figsize=(10, 8))
plt.hist([charged_off_loans['grade'], behind_loans['grade']], label=['Charged Off', 'Behind'])
plt.legend(loc='upper right')
plt.title('Grade Distribution')
plt.show()

plt.figure(figsize=(10, 8))
plt.hist([charged_off_loans['purpose'], behind_loans['purpose']], label=['Charged Off', 'Behind'])
plt.legend(loc='upper right')
plt.title('Purpose Distribution')
plt.show()

plt.figure(figsize=(10, 8))
plt.hist([charged_off_loans['dti'], behind_loans['dti']], label=['Charged Off', 'Behind'])
plt.legend(loc='upper right')
plt.title('DTI Distribution')
plt.show()