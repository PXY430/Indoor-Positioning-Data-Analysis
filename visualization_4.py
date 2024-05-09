import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.colors import Normalize
import numpy as np

file_path = '0703_.csv'

df = pd.read_csv(file_path)

# Select all WAP columns and replace the value of 100 with NaN (assuming 100 represents no signal)
wap_columns = [col for col in df.columns if 'WAP' in col]
df[wap_columns] = df[wap_columns].replace(100, np.nan)

# Calculate the number of active APs at each location
df['Active_AP_Count'] = df[wap_columns].notna().sum(axis=1)

# Plot a heatmap
plt.figure(figsize=(15, 10))
scatter = plt.scatter(df['x'], df['y'], c=df['Active_AP_Count'], cmap='viridis',
                      norm=Normalize(vmin=df['Active_AP_Count'].min(), vmax=df['Active_AP_Count'].max()),
                      alpha=0.6, edgecolors='w', s=80)

# Display the color bar and set its label
cbar = plt.colorbar(scatter, shrink=0.5)
cbar.set_label('Number of Active APs', fontsize=10)

# Set x and y axes ticks to unique values in the dataset
plt.xticks(sorted(df['x'].unique()), rotation=45, fontsize=8)
plt.yticks(sorted(df['y'].unique()), fontsize=8)

# Set axes to have the same scale
plt.gca().set_aspect('equal', adjustable='box')

plt.grid(True, which='both', linestyle='--', linewidth=0.5)

plt.xlabel('X Coordinate', fontsize=14)
plt.ylabel('Y Coordinate', fontsize=14)
plt.title('SC_floor4_0703', fontsize=16)

plt.tight_layout()

plt.show()
