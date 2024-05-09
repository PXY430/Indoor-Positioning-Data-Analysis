import pandas as pd
import matplotlib.pyplot as plt
import glob
import os
from datetime import datetime

folder_path = r'C:\Users\PXY\Documents\WeChat Files\wxid_rn5clc228mxo12\FileStorage\File\2024-03\SC(2)\SC\floor5'
file_pattern = os.path.join(folder_path, '*.csv')

csv_files = glob.glob(file_pattern)

max_non_100_values = []

# List of dates with rainy weather
rainy_dates = ['2023-06-30', '2023-07-02', '2023-07-06', '2023-07-08', '2023-07-09', '2023-07-16', '2023-07-20', '2023-07-29', '2023-08-16', '2023-08-18']

for file_path in csv_files:
    df = pd.read_csv(file_path)
    date_str = os.path.basename(file_path).split('.')[0]  # Assuming the file name format is 'MMDD.csv'
    # Convert date string to datetime object
    date = datetime.strptime('2023' + date_str, '%Y%m%d').date()

    if 'WAP0373' in df.columns:
        wap_data = df['WAP0373'][df['WAP0373'] != 100]
        max_value = wap_data.max() if not wap_data.empty else None
        max_non_100_values.append({'Date': date, 'Max_Non100_Value': max_value})

# Convert list to DataFrame and assign column names
results_df = pd.DataFrame(max_non_100_values)

# Sort DataFrame by date
results_df.sort_values('Date', inplace=True)

# Plot a bar chart
plt.figure(figsize=(15, 7))
for index, row in results_df.iterrows():
    color = 'green' if str(row['Date']) in rainy_dates else 'blue'
    plt.bar(row['Date'], row['Max_Non100_Value'], color=color)

# Calculate the overall average and rainy day average
overall_mean = results_df['Max_Non100_Value'].mean()
rainy_days_df = results_df[results_df['Date'].astype(str).isin(rainy_dates)]
rainy_days_mean = rainy_days_df['Max_Non100_Value'].mean()

# Add horizontal lines for overall average and rainy day average
plt.axhline(y=overall_mean, color='red', linestyle='--', label='Overall Mean')
plt.axhline(y=rainy_days_mean, color='purple', linestyle='--', label='Rainy Days Mean')

plt.legend()

plt.title('Maximum Non-100 Values for WAP0373 over Time')
plt.xlabel('Date')
plt.ylabel('Maximum Value')

plt.xticks(results_df['Date'], rotation=90, fontsize=8)

plt.grid(True)
plt.tight_layout()
plt.show()
