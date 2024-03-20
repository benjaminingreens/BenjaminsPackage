import pandas as pd
from collections import defaultdict

# ------------
# INITIALISATIONS
# ------------

# Reads a csv to a dataframe
def read_csv_to_df(csv_path):
   
   df = pd.read_csv(csv_path)
   
   return df

# Initialises a csv into a 'ready-to-use' dataframe by also ordering it according to a selection of columns and ensuring the right columns are numeric
def init_csv_as_ready_df(column_list, round_num, csv_path='', start_column='', end_column=''):
   
   # Reads the CSV into a pandas dataframe
   df = pd.read_csv(csv_path)
   
   # Removes leading & trailing whitespace from all column names
   df.columns = [col.strip() for col in df.columns]
   
   # Gets only specified columns from dataframe
   df = df[column_list]
   
   # Converts specified columns to numeric
   start_index = df.columns.get_loc(start_column)
   end_index = df.columns.get_loc(end_column)
   
   for col in df.columns [start_index:end_index + 1]:
      df.loc[:, col] = pd.to_numeric(df.loc[:, col], errors='coerce').round(round_num)
   
   return df

# Initialises a dataframe into a 'ready-to-use' dataframe by also ordering it according to a selection of columns and ensuring the right columns are numeric
def init_df_as_ready_df(df, column_list, round_num, start_column='', end_column=''):
   
   # Removes leading & trailing whitespace from all column names
   df.columns = [col.strip() for col in df.columns]
   
   # Gets only specified columns from dataframe
   df = df[column_list]
   
   # Converts specified columns to numeric
   start_index = df.columns.get_loc(start_column)
   end_index = df.columns.get_loc(end_column)
   
   for col in df.columns [start_index:end_index + 1]:
      df.loc[:, col] = pd.to_numeric(df.loc[:, col], errors='coerce').round(round_num)
   
   return df

# ------------
# CHECKS AND BALANCES
# ------------

# Checks for duplicates in a column and returns a dictionary of duplicates in the column (where the key is the duplicate item, and the value is a list of row numbers where that duplicate item can be found)
def check_for_duplicates(df, column=''):
   
   # Not sure what this actually does lol
   duplicates_dict = defaultdict(list)
   
   # Iterate through index and value in the column and store them in the dictionary
   # I have added 2 to the index value, because the index value + 2 is equal to the row number in the csv file which the dataframe might have come from
   for index, value in df[column].items():
      duplicates_dict[value].append(index + 2)
   
   # Keep only duplicate values, and store their indexes (row numbers) in the value of the dictionary
   duplicates_dict = {key: val for key, val in duplicates_dict.items() if len(val) > 1}
   
   return duplicates_dict

# ------------
# PROCESSING OPERATIONS
# ------------

# Removes rows with a certain value in a certain column and returns the dataframe with the removed rows
def remove_rows_with_value(df, value, column=''):
   
   df = df[df[column] != value]
   
   return df

# This filters a dataframe according to a certain value in a specified column, and then it returns the filtered dataframe
def filter_df(df, value, column=''):
   
   filtered_df = df[df[column] == value]
   
   return filtered_df

# This filters a dataframe according to whether or not a certain value contains 'X' in a specified column, and then it returns the filtered dataframe. This is a case insensitive version
def filter_df_contains(df, value, column=''):
   
   filtered_df = df[df[column].str.contains(value, case=False, na=False)]
   
   return filtered_df

# This filters a dataframe according to whether or not a certain value contains 'X' in a specified column, and then it returns the filtered dataframe. This is a case sensitive version
def filter_df_CONTAINS(df, value, column=''):
   
   filtered_df = df[df[column].str.contains(value, case=False, na=False)]
   
   return filtered_df
