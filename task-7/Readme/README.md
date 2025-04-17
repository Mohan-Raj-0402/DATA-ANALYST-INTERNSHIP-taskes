## 📊 Task 7 – Get Basic Sales Summary from a Tiny SQLite Database using Python 

#### 🔍 Objective

The goal of this task was to analyze a small sales dataset using SQL queries inside Python. The final output includes a summary of total quantities and revenue per product, printed to the console and visualized using both Matplotlib and Plotly (2D & 3D). 

---

#### 💠 Tools Used

- Python 
- SQLite3 
- Pandas 
- Matplotlib & Plotly 
- Jupyter Notebook 📓

---

#### 🧠 What I Did

1. **Created a SQLite database** (`sales_data.db`) with a `sales` table.
2. **Inserted multiple product sales records**, including realistic quantity and price variations.
3. **Executed SQL query** to get total quantity and revenue for each product:
   ```sql
   SELECT product, SUM(quantity) AS total_qty, SUM(quantity * price) AS revenue
   FROM sales
   GROUP BY product;
   ```
4. **Loaded SQL result into a Pandas DataFrame**
5. **Displayed the result using print()**
6. **Visualized data**:
   - Bar chart using Matplotlib
   - 3D bar and scatter plots using Plotly


---

#### 📁 Files Included

| File | Description |
|------|-------------|
| `Basic Sales Summary from a Tiny SQLite Database using Python.ipynb` | Main Jupyter Notebook with all steps |
| `sales_data.db` | SQLite database |
| `sales_chart.png` | 2D bar chart (Matplotlib) |
| `sales_chart_3d.png` | 3D bar chart (Matplotlib) |
| `sales_summary.csv` | Data exported for Power BI |
| `README.md` | This file! ✔️

---

#### 📷 Screenshots

![newplot](https://github.com/user-attachments/assets/adb76e2e-aeb1-4136-ba5f-84f402f55ad6)

![3D Revenue by Product](https://github.com/user-attachments/assets/7ced47c3-f671-42de-8f33-e98ebdb15203)

---
