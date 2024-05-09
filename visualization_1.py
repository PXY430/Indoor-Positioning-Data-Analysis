import pandas as pd
import matplotlib.pyplot as plt

file_path = '0703_.csv'

df = pd.read_csv(file_path)

# Extract and sort unique values from x and y columns
unique_x = sorted(df['x'].unique())
unique_y = sorted(df['y'].unique())

plt.figure(figsize=(10, 10))

plt.scatter(df['x'], df['y'], alpha=0.6, edgecolors='w', s=80)

def set_x_ticks(x_values):

    ticks_to_show = {x_values[0]}

    for x in x_values[1:]:
        if all(abs(x - shown) >= 30 for shown in ticks_to_show):
            ticks_to_show.add(x)
    return sorted(ticks_to_show)

x_ticks_to_show = set_x_ticks(unique_x)
plt.xticks(x_ticks_to_show, rotation=90, fontsize=5)

plt.yticks(unique_y, fontsize=5)

plt.gca().set_aspect('equal', adjustable='box')

plt.grid(True, which='both', linestyle='--', linewidth=0.5)

plt.axhline(y=0, color='k', linewidth=1.5)
plt.axvline(x=0, color='k', linewidth=1.5)

plt.xlabel('X Coordinate', fontsize=14)
plt.ylabel('Y Coordinate', fontsize=14)

plt.title('SC_0727', fontsize=16)

plt.tight_layout()

plt.show()
