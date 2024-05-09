import pandas as pd
import matplotlib.pyplot as plt
import glob
import os
from datetime import datetime

folder_path = r'C:\Users\PXY\Documents\WeChat Files\wxid_rn5clc228mxo12\FileStorage\File\2024-03\SC(2)\SC\floor5'
file_pattern = os.path.join(folder_path, '*.csv')

csv_files = glob.glob(file_pattern)

time_active_wap_counts = []

for file_path in csv_files:
    df = pd.read_csv(file_path)

    date_str = os.path.basename(file_path).split('.')[0]
    # Convert the date string into a datetime object
    date = datetime.strptime('2023' + date_str, '%Y%m%d').date()

    # Remove all WAP columns with a value of 100
    wap_columns = [col for col in df.columns if col.startswith('WAP') and df[col].nunique() > 1]
    df = df[wap_columns]

    # Select all WAP columns and calculate if there are any non-100 values
    wap_columns = [col for col in df.columns if 'WAP' in col]
    # Count the number of WAP columns not equal to 100
    active_wap_count = (df[wap_columns] != 100).any(axis=0).sum()

    time_active_wap_counts.append({'Date': date, 'Active_WAP_Count': active_wap_count})

# Convert list to DataFrame and name the columns
active_wap_df = pd.DataFrame(time_active_wap_counts)

print(active_wap_df.columns)

# Convert list to DataFrame
active_wap_df = pd.DataFrame(time_active_wap_counts)

# Sort by date
active_wap_df.sort_values('Date', inplace=True)

# Plot a bar chart
plt.figure(figsize=(15, 7))
plt.bar(active_wap_df['Date'], active_wap_df['Active_WAP_Count'], color='blue')

plt.title('SC_floor5')
plt.xlabel('Date')
plt.ylabel('Number of Active WAPs')

plt.xticks(active_wap_df['Date'], rotation=90, fontsize=8)

plt.grid(True)
plt.tight_layout()
plt.show()
