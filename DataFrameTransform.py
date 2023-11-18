import numpy as np
import pandas as pd 
from pandas.tseries.offsets import DateOffset
from scipy.special import boxcox1p
from scipy.stats import zscore

class DataTransform:
    def __init__(self, df):
        self.df = df

    def transform_dtypes(self):
        # Convert 'term' to int64
        self.df['term'] = self.df['term'].astype(str).str.strip().str.replace(' months', '')
        self.df['term'] = pd.to_numeric(self.df['term'], errors='coerce').fillna(0).astype('int64')

        # Convert 'employment_length' to int64
        self.df['employment_length'] = self.df['employment_length'].astype(str).replace('nan', '0').apply(self.convert_emp_length).fillna(0).astype('int64')

        # Convert 'sub_grade' to int64
        self.df['sub_grade'] = pd.to_numeric(self.df['sub_grade'], errors='coerce').fillna(0)

        # Convert 'home_ownership', 'verification_status', 'loan_status', 'payment_plan', 'purpose' to categorical
        for column in ['home_ownership', 'verification_status', 'loan_status', 'payment_plan', 'purpose', 'application_type', 'grade']:
            self.df[column] = pd.Categorical(self.df[column])

        # Convert 'issue_date', 'earliest_credit_line', 'last_payment_date', 'next_payment_date', 'last_credit_pull_date' to datetime64
        for column in ['issue_date', 'earliest_credit_line', 'last_payment_date', 'next_payment_date' , 'last_credit_pull_date']:
            self.df[column] = pd.to_datetime(self.df[column], errors='coerce')
        
    def preprocess_date(date_str):
       # Add your preprocessing logic here
       # For example, if your dates are in the format 'dd-mm-yyyy' or 'dd/mm/yyyy', you can do:
        date_str = date_str.replace('-', '/')

       # Then, try to convert the preprocessed string to a date
        try:
            return pd.to_datetime(date_str, format='%d/%m/%Y')
        except ValueError:
        # If the conversion fails, return the original string
            return date_str

       # Apply the preprocessing function to each date in the column
        df['next_payment_date'] = df['next_payment_date'].apply(preprocess_date)
    

    @staticmethod
    def convert_emp_length(emp_length_str):
       """
       Converts employment length to an integer.

       Parameters
       ----------
       emp_length_str : str
       a string representing employment length

       Returns
       -------
       int
            an integer representing employment length
      """

       if emp_length_str is None or emp_length_str.strip() == 'None':
          return None
       elif emp_length_str.strip() in ['< 1 year', '1 year']:
          return 0
       elif emp_length_str.strip() == '10+ years':
          return 10
       else:
           return int(emp_length_str.replace(' years', ''))


    def drop_columns(self):
        # Drop specified columns
        columns_to_drop = ['mths_since_last_delinq', 'mths_since_last_record','mths_since_last_major_derog']
        self.df = self.df.drop(columns=columns_to_drop)


    def handle_nulls(self):
        # Fill missing values in 'int_rate', 'last_payment_date', 'last_credit_pull_date', 'collections_12_mths_ex_med' with median
        for column in ['int_rate','funded_amount', 'last_payment_date', 'last_credit_pull_date', 'collections_12_mths_ex_med']:
            self.df[column].fillna(self.df[column].median(), inplace=True)

    def transform_skewed_cols(self, skew_threshold=0.50, lam=0.15):
       """Transforms skewed columns in the DataFrame."""
       # Calculate skewness
       skewness = self.df.skew(axis = 0, skipna = True, numeric_only=True)

       # Identify skewed columns
       skewed_cols = skewness[skewness.abs() > skew_threshold].index

       # Apply Box-Cox transformation to each skewed column
       for col in skewed_cols:
            self.df[col] = boxcox1p(self.df[col], lam)
    
    def fix_next_payment_date(self):
        self.df['next_payment_date'] = self.df['last_payment_date'] + DateOffset(months=1)

    def handle_outliers(self, cols, method='zscore', threshold=3):
        """
        Handles outliers in the DataFrame.

        Parameters
        ----------
        cols : list
            a list of column names to handle outliers
        method : str, optional
            the method to use for outlier detection ('zscore' or 'iqr')
        threshold : float, optional
            the threshold for outlier detection
        """
        if method == 'zscore':
            for col in cols:
                self.df = self.df[(np.abs(zscore(self.df[col])) < threshold)]
        elif method == 'iqr':
            for col in cols:
                Q1 = self.df[col].quantile(0.25)
                Q3 = self.df[col].quantile(0.75)
                IQR = Q3 - Q1
                self.df = self.df[~((self.df[col] < (Q1 - 1.5 * IQR)) | (self.df[col] > (Q3 + 1.5 * IQR)))]
        else:
            raise ValueError("Method must be either 'zscore' or 'iqr'")

    def save_to_csv(self, filename):
        """
        Saves the DataFrame to a new CSV file.

        Parameters
        ----------
            filename : str
                The name of the file to save the DataFrame to.
        """
        self.df.to_csv(filename, index=False)

df = pd.read_csv(r'C:\Users\Louis\Aicore\Dataset_loan_project\loan_payments.csv')

data_transform = DataTransform(df)
data_transform.transform_dtypes()
data_transform.drop_columns()
data_transform.handle_nulls()
data_transform.transform_skewed_cols()
data_transform.fix_next_payment_date()
data_transform.handle_outliers(cols=['total_rec_late_fee'], method='zscore', threshold=3)
data_transform.save_to_csv('transformed_data.csv')


 
