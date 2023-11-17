import os
import sqlalchemy
import yaml
import pandas as pd
from pandas.io.sql import read_sql_table
from sqlalchemy import create_engine, inspect
import psycopg2
from psycopg2 import sql


class RdsDatabaseConnecter:
    '''
     A class to connect to an RDS Database and perform various operations
    '''
    def __init__(self, credentials_file):
        '''
        Initialize a connection to the RDS Database with a credentials file
        '''
        self.credentials_dict = self.read_credentials(credentials_file)
        self.engine = self.get_connection()

    def read_credentials(self, file):
        '''
        Reads the credentials file from a given file
        '''
        with open(file, mode="r") as file:
            credentials_dict = yaml.safe_load(file)
        return credentials_dict

    def get_connection(self):
        '''
        Get a connection the the RDS Database using the credentials

        '''
        return create_engine(
            f"postgresql+psycopg2://{self.credentials_dict['RDS_USER']}:{self.credentials_dict['RDS_PASSWORD']}@{self.credentials_dict['RDS_HOST']}:{self.credentials_dict['RDS_PORT']}/{self.credentials_dict['RDS_DATABASE']}")

    def get_table_names(self):
        '''
        Get all the names of the tables in the RDS Database
        '''
        inspector = inspect(self.engine)
        return inspector.get_table_names()

    def extract_data(self, table_name):
        '''
         Extract the data from the given table in the RDS Database
        '''
        conn = psycopg2.connect(dbname=self.credentials_dict['RDS_DATABASE'], user=self.credentials_dict['RDS_USER'], password=self.credentials_dict['RDS_PASSWORD'], host=self.credentials_dict['RDS_HOST'], port=self.credentials_dict['RDS_PORT'])
        cur = conn.cursor()
        query = sql.SQL("SELECT * FROM {}").format(sql.Identifier(table_name))
        cur.execute(query)
        rows = cur.fetchall()
        df = pd.DataFrame(rows, columns=[desc[0] for desc in cur.description])
        conn.close()
        return df

    def save_data_to_csv(self, df, filename):
        '''
         Save the given DataFrame to a CSV file with the given filename
        '''
        if not filename.endswith('.csv'):
            filename += '.csv'
        df.to_csv(filename, index=False)
        print(f"Data saved to {os.path.abspath(filename)}")

if __name__ == '__main__':
    '''
    Main function to execute the script with error handling
    '''
    try:
        rds = RdsDatabaseConnecter('credentials.yaml')
        print(f"Connection to the {rds.credentials_dict['RDS_HOST']} for user {rds.credentials_dict['RDS_USER']} created successfully.")
        df = rds.extract_data('loan_payments')
        print("Data from table 'loan_payments':")
        print(df)
        rds.save_data_to_csv(df, 'loan_payments.csv')
    except Exception as ex:
        print("An error occurred: \n", ex)


