import pandas as pd
import matplotlib.pyplot as plt
import glob
import os
from datetime import datetime

folder_path = r'C:\Users\PXY\Documents\WeChat Files\wxid_rn5clc228mxo12\FileStorage\File\2024-03\SC(2)\SC\floor5'
file_pattern = os.path.join(folder_path, '*.csv')

csv_files = glob.glob(file_pattern)

max_non_100_values = []

for file_path in csv_files:
    df = pd.read_csv(file_path)
    date_str = os.path.basename(file_path).split('.')[0]  # Assuming the file is formatted like 'MMDD.csv'

    # Convert the date string into a datetime object
    date = datetime.strptime('2023' + date_str, '%Y%m%d').date()

    if 'WAP0371' in df.columns:
        wap_data = df['WAP0371'][df['WAP0371'] != 100]
        max_value = wap_data.max() if not wap_data.empty else None
        max_non_100_values.append({'Date': date, 'Max_Non100_Value': max_value})

# Convert the list to DataFrame and name the columns
results_df = pd.DataFrame(max_non_100_values)

# Sort by date
results_df.sort_values('Date', inplace=True)

# Plot a bar chart
plt.figure(figsize=(15, 7))
plt.bar(results_df['Date'], results_df['Max_Non100_Value'], color='blue')

plt.title('Maximum Non-100 Values for WAP0371 over Time')
plt.xlabel('Date')
plt.ylabel('Maximum Value (Non-100)')

plt.xticks(results_df['Date'], rotation=90, fontsize=8)

plt.grid(True)
plt.tight_layout()
plt.show()
