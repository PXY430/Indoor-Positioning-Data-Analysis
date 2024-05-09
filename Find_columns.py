import pandas as pd
import glob
import os

# Set the folder path
folder_path = r'C:\Users\PXY\Documents\WeChat Files\wxid_rn5clc228mxo12\FileStorage\File\2024-03\SC(2)\SC\floor5'
# Match all CSV files
file_pattern = os.path.join(folder_path, '*.csv')
files = glob.glob(file_pattern)

# Initialize a list to store valid AP columns for each file
common_columns = None

for file in files:
    df = pd.read_csv(file)
    # Filter columns that start with 'WAP' and have values between -100 and 0
    valid_columns = [col for col in df if col.startswith('WAP') and df[col].between(-100, 0).any()]
    # If it is the first file, initialize common_columns
    if common_columns is None:
        common_columns = set(valid_columns)
    else:
        # For subsequent files, find common columns
        common_columns.intersection_update(valid_columns)

# Convert the results to a list and print
common_columns = list(common_columns)
print("Result:", common_columns)
