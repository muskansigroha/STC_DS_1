# 📊 Task 1 - Population Visualization using World Bank Data

## 📝 Objective
Create visualizations to understand population distribution using real-world data from the World Bank and simulated demographic data.

---

## 📁 Dataset
- Source: World Bank Open Data
- File: `API_SP.POP.TOTL_DS2_en_csv_v2_399596.zip`

---

## ✅ Tasks Covered
1. **Extract and Read Data**
   - Extract `.csv` from `.zip`
   - Load using `pandas`

2. **Data Cleaning & Transformation**
   - Convert wide to long format
   - Remove missing/null values
   - Convert year to integer

3. **Visualizations**
   - 📈 Bar Chart: Top 10 most populous countries (2022)
   - 📊 Histogram: Simulated age distribution of a sample population
   - 🧍‍♂️🧍‍♀️ Count Plot: Simulated gender distribution
   - 🗺 Choropleth Map: Global population by country (2022)

---

## 🛠 Libraries Used
- `pandas`
- `matplotlib`
- `seaborn`
- `plotly`
- `numpy`
- `zipfile`
- `os`

---

## 🚀 How to Run
1. Download the ZIP file from the World Bank.
2. Replace the ZIP path in the script with your own local path.
3. Run the script in a Python environment (Jupyter Notebook recommended).

---

## 📷 Output Previews
- Bar chart for top 10 countries
- Histogram of simulated age data
- Count plot of gender
- Interactive choropleth world map

---

## 📌 Notes
- For age and gender plots, synthetic data is generated using `numpy`.
- Choropleth uses ISO country codes for mapping.

---

## 📎 License
Data © World Bank Group. Code © YourNameHere 2025.
