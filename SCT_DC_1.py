# Task 1: Population Data Visualization
# Author: [Muskan Sigroha]
# Dataset Source: World Bank (Total Population)
# Description: This script extracts population data from a zip file, processes it, and visualizes it using Matplotlib, Seaborn, and Plotly.

import os
import zipfile
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import plotly.express as px

# --------------------- Step 1: Extract ZIP File ---------------------
# Define relative paths
zip_path = "API_SP.POP.TOTL_DS2_en_csv_v2_2590.zip"
extract_path = "population_data"

# Make sure the directory exists
os.makedirs(extract_path, exist_ok=True)

# Extract ZIP contents
with zipfile.ZipFile(zip_path, 'r') as zip_ref:
    zip_ref.extractall(extract_path)

# Print extracted files
print("Extracted files:", os.listdir(extract_path))

# --------------------- Step 2: Load CSV ---------------------
csv_file = "API_SP.POP.TOTL_DS2_en_csv_v2_2590.csv"
csv_path = os.path.join(extract_path, csv_file)

# Read CSV file (skip metadata rows)
df_raw = pd.read_csv(csv_path, skiprows=4)

print("Raw Data Preview:\n", df_raw.head())

# --------------------- Step 3: Transform Data ---------------------
df_long = df_raw.melt(
    id_vars=['Country Name', 'Country Code', 'Indicator Name', 'Indicator Code'],
    var_name='Year',
    value_name='Population'
)

# Convert year and population columns
df_long['Year'] = pd.to_numeric(df_long['Year'], errors='coerce')
df_long['Population'] = pd.to_numeric(df_long['Population'], errors='coerce')
df_long.dropna(subset=['Year', 'Population'], inplace=True)
df_long['Year'] = df_long['Year'].astype(int)

print("Transformed Data Preview:\n", df_long.head())

# --------------------- Step 4: Top 10 Most Populous Countries (2022) ---------------------
df_2022 = df_long[df_long['Year'] == 2022]
top10 = df_2022.sort_values(by='Population', ascending=False).head(10)

plt.figure(figsize=(12, 6))
sns.barplot(data=top10, x='Country Name', y='Population', palette='viridis')
plt.title("Top 10 Most Populous Countries (2022)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("top10_population_2022.png")
plt.show()

# --------------------- Step 5: Simulated Age Distribution ---------------------
np.random.seed(42)
ages = np.random.normal(loc=35, scale=10, size=1000)

plt.figure(figsize=(10, 6))
sns.histplot(ages, bins=20, kde=True, color='skyblue')
plt.title("Age Distribution of Sample Population")
plt.xlabel("Age")
plt.ylabel("Number of People")
plt.grid(True)
plt.tight_layout()
plt.savefig("age_distribution.png")
plt.show()

# --------------------- Step 6: Simulated Gender Distribution ---------------------
genders = np.random.choice(['Male', 'Female'], size=1000, p=[0.52, 0.48])

plt.figure(figsize=(6, 4))
sns.countplot(x=genders, palette='Set2')
plt.title("Gender Distribution in Sample Population")
plt.xlabel("Gender")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig("gender_distribution.png")
plt.show()

# --------------------- Step 7: Choropleth Map ---------------------
fig = px.choropleth(
    df_2022,
    locations="Country Code",
    color="Population",
    hover_name="Country Name",
    color_continuous_scale=px.colors.sequential.Plasma,
    title="Global Population Distribution (2022)",
    projection="natural earth",
    template="plotly_dark"
)

fig.write_html("population_map_2022.html")
fig.show()
# --------------------- Step 8: Save Processed Data ---------------------
df_long.to_csv("processed_population_data.csv", index=False)