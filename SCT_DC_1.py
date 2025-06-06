# SCT_DC_1: Bar Chart to Visualize Population Distribution (World Bank Data)

import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset (update the path if needed)
file_path = 'API_SP.POP.TOTL_DS2_en_csv_v2_2590.csv'
df = pd.read_csv(file_path, skiprows=4)

# Select relevant columns: Country Name and Population in 2023
population_2023 = df[['Country Name', '2023']].dropna()

# Get top 20 countries by population in 2023
top_20_population = population_2023.sort_values(by='2023', ascending=False).head(20)

# Create a horizontal bar chart
plt.figure(figsize=(12, 8))
plt.barh(top_20_population['Country Name'], top_20_population['2023'], color='skyblue')
plt.xlabel('Population in 2023')
plt.title('Top 20 Most Populous Countries in 2023')
plt.gca().invert_yaxis()  # Largest bar on top
plt.grid(axis='x', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
