import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.colors import Normalize
import numpy as np

file_path = '0703_.csv'

df = pd.read_csv(file_path)

no_signal = df[df['WAP0304'] == 100][['x', 'y']]

df_filtered = df[df['WAP0304'] != 100]

# Extract and sort unique values from x and y columns
unique_x = sorted(df_filtered['x'].unique())
unique_y = sorted(df_filtered['y'].unique())

def set_x_ticks(x_values):
    ticks_to_show = {x_values[0]}
    for x in x_values[1:]:
        if all(abs(x - shown) >= 5 for shown in ticks_to_show):
            ticks_to_show.add(x)
    return sorted(ticks_to_show)

x_ticks_to_show = set_x_ticks(unique_x)

plt.figure(figsize=(15, 10))

scatter = plt.scatter(df_filtered['x'], df_filtered['y'], c=df_filtered['WAP0304'], cmap='jet',
                      norm=Normalize(vmin=df_filtered['WAP0304'].min(), vmax=df_filtered['WAP0304'].max()),
                      alpha=0.6, edgecolors='w', s=80)

# Plot positions without signal using red crosses
plt.scatter(no_signal['x'], no_signal['y'], color='red', marker='x', label='No Signal')

cbar = plt.colorbar(scatter, shrink=0.5)
cbar.set_label('Average Signal Strength', fontsize=10)
cbar.ax.locator_params(nbins=10)

plt.xticks(x_ticks_to_show, rotation=45, fontsize=8)
plt.yticks(unique_y, fontsize=8)

plt.gca().set_aspect('equal', adjustable='box')

plt.grid(True, which='both', linestyle='--', linewidth=0.5)

plt.xlabel('X Coordinate', fontsize=14)
plt.ylabel('Y Coordinate', fontsize=14)

plt.title('SC_0703_WAP0304', fontsize=16)
plt.legend()

plt.tight_layout()

plt.show()
