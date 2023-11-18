import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

class Plotter:
    """
    A class used to plot various aspects of a DataFrame.

    ...

    Attributes
    ----------
    df : DataFrame
        a pandas DataFrame containing the data to be plotted

    Methods
    -------
    plot_null_removal():
        Plots the number of NULL values in each column before and after removal.
    plot_skewness(skew_threshold=0.50):
        Plots the distribution of each column with skewness greater than a specified threshold.
    """

    def __init__(self, df):
        """
        Constructs all the necessary attributes for the Plotter object.

        Parameters
        ----------
            df : DataFrame
                a pandas DataFrame containing the data to be plotted
        """

        self.df = df

    def plot_null_removal(self):
        """
        Plots the number of NULL values in each column before and after removal.
        """

        # Count the number of NULL values in each column before removal
        before_removal = self.df.isnull().sum()

        # Remove NULL values
        df_removed = self.df.dropna()

        # Count the number of NULL values in each column after removal
        after_removal = df_removed.isnull().sum()

        # Create a DataFrame from the before and after Series
        df_plot = pd.DataFrame({'Before Removal': before_removal, 'After Removal': after_removal})

        # Create the plot
        df_plot.plot(kind='bar', figsize=(12, 6))
        plt.title('NULL Values Before and After Removal')
        plt.ylabel('Number of NULL Values')
        plt.show()

    def plot_skewness(self, skew_threshold=0.50):
        """
        Plots the distribution of each column with skewness greater than a specified threshold.

        Parameters
        ----------
        skew_threshold : float, optional
            the skewness threshold for plotting (default is 0.50)
        """

        # Calculate skewness
        skewness = self.df.skew(axis = 0, skipna = True, numeric_only=True)

        # Identify skewed columns
        skewed_cols = skewness[skewness.abs() > skew_threshold].index

        # Plot each skewed column
        for col in skewed_cols:
            sns.histplot(self.df[col], kde=True)
            plt.title(f'Skewness of {col}')
            plt.show()

# Load your data into a DataFrame
df = pd.read_csv(r'C:\Users\Louis\Aicore\Dataset_loan_project\transformed_df.csv') 

# Create an instance of the Plotter class
plotter = Plotter(df)
plotter.plot_null_removal()
# Plot skewness
plotter.plot_skewness(skew_threshold=0.50)








