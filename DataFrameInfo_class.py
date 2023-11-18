import pandas as pd
import numpy as np

class DataFrameInfo:
    """
    A class used to extract information from a DataFrame.

    ...

    Attributes
    ----------
    df : pandas.DataFrame
        a pandas DataFrame containing the data

    Methods
    -------
    describe_all()
        Describes all columns in the DataFrame.
    get_median()
        Returns the median of the DataFrame.
    get_std_dev()
        Returns the standard deviation of the DataFrame.
    get_mean()
        Returns the mean of the DataFrame.
    count_distinct()
        Returns the count of distinct values in each column.
    print_shape()
        Prints the shape of the DataFrame.
    count_nulls()
        Returns the count of NULL values in each column.
    percent_nulls()
        Returns the percentage of NULL values in each column.
    """

    def __init__(self, df):
        """
        Constructs all the necessary attributes for the DataFrameInfo object.

        Parameters
        ----------
            df : pandas.DataFrame
                a pandas DataFrame containing the data
        """

        self.df = df

    def describe_all(self):
     """Describes all columns in the DataFrame."""
     if isinstance(self.df, pd.DataFrame):
        return self.df.describe(include='all', datetime_is_numeric=True)
     else:
        return "The 'df' attribute must be a pandas DataFrame."

    def get_median(self):
        """Returns the median of the DataFrame."""
        return self.df.median(numeric_only=True)

    def get_std_dev(self):
        """Returns the standard deviation of the DataFrame."""
        return self.df.std(numeric_only=True)

    def get_mean(self):
        """Returns the mean of the DataFrame."""
        return self.df.mean(numeric_only=True)

    def count_distinct(self):
        """Returns the count of distinct values in each column."""
        return self.df.nunique()

    def print_shape(self):
        """Prints the shape of the DataFrame."""
        print(f'The DataFrame has {self.df.shape[0]} rows and {self.df.shape[1]} columns.')

    def count_nulls(self):
        """Returns the count of NULL values in each column."""
        return self.df.isnull().sum()

    def percent_nulls(self):
        """Returns the percentage of NULL values in each column."""
        return self.df.isnull().mean() * 100

# Load your data into a DataFrame. Replace '/content/transformed_df.csv' with the path to your actual CSV file.
df = pd.read_csv('/content/transformed_data.csv')

# Now you can create an instance of DataFrameInfo
df_info = DataFrameInfo(df)

# Now you can use the methods of the DataFrameInfo class to extract information from your DataFrame

# To get a description of all columns in the DataFrame
print("Description of all columns in the DataFrame:")
print(df_info.describe_all())

# To get the median of the DataFrame
print("\nMedian of the DataFrame:")
print(df_info.get_median())

# To get the standard deviation of the DataFrame
print("\nStandard deviation of the DataFrame:")
print(df_info.get_std_dev())

# To get the mean of the DataFrame
print("\nMean of the DataFrame:")
print(df_info.get_mean())

# To get the count of distinct values in each column
print("\nCount of distinct values in each column:")
print(df_info.count_distinct())

# To print the shape of the DataFrame
print("\nShape of the DataFrame:")
df_info.print_shape()

# To get the count of NULL values in each column
print("\nCount of NULL values in each column:")
print(df_info.count_nulls())

# To get the percentage of NULL values in each column
print("\nPercentage of NULL values in each column:")
print(df_info.percent_nulls())
