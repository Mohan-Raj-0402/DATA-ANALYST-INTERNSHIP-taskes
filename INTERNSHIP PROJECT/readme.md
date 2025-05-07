# E-commerce Return Rate Reduction Analysis

## 📌 Objective
The goal of this project is to analyze why customers return products and understand how return rates vary across:
- Product categories
- Geographic regions
- Marketing and payment channels

Ultimately, the objective is to **reduce return rates** and **improve customer satisfaction**.

---

## 🛠 Tools & Technologies
- **Python**: Data cleaning, feature engineering, and logistic regression modeling.
- **SQL**: Analytical queries on returns by category, region, and payment mode.
- **Power BI**: Interactive dashboard for visual analytics and return risk scoring.

---

## 📂 Dataset Overview
The dataset includes fictional sales and returns data from a SuperStore, with fields such as:
- **Order Info**: Order ID, Order Date, Ship Date, Ship Mode
- **Customer Info**: Customer ID, Segment, City, State, Region
- **Product Info**: Product ID, Name, Category
- **Sales Info**: Quantity, Price, Profit, Total Sales
- **Return Info**: Returns (0 = Not Returned, 1 = Returned)
- **Payment Info**: Payment Mode

---

## 🧹 Step 1: Data Cleaning (Python)
- Removed duplicates and missing values
- Converted `order_date` and `ship_date` to datetime format
- Encoded categorical features
- Verified `returns` as a binary target variable
- Saved the cleaned data as a CSV for modeling and Power BI

---

## 📊 Step 2: Return Rate Analysis (SQL)
Analyzed return rates using SQL queries:

### Return Rate by Category:
| Category        | Return Rate (%) |
|----------------|------------------|
| Technology      | 12.4%            |
| Furniture       | 9.3%             |
| Office Supplies | 7.1%             |

### Return Rate by Region:
| Region  | Return Rate (%) |
|---------|------------------|
| West    | 11.8%            |
| East    | 9.5%             |
| South   | 8.7%             |
| Central | 6.9%             |

### Return Rate by Payment Mode:
| Payment Mode | Return Rate (%) |
|--------------|------------------|
| Online       | 12.5%            |
| Credit Card  | 10.2%            |
| Cash         | 9.1%             |

---

## 🔍 Step 3: Predictive Modeling (Python)
Built a logistic regression classifier to predict return probability.

### Features:
- Category, Region, Segment
- Ship Mode, Payment Mode
- Quantity, Price, Profit

### Target:
- `Returns` (1 = Returned, 0 = Not Returned)

### Model Performance:
- **Accuracy**: 84.2%
- **ROC AUC**: 0.78
- Exported `return_probability` for all products

Products with `return_probability > 0.6` were flagged as high-risk and saved to a CSV.

---

## 📈 Power BI Dashboard
Created a dynamic dashboard with the following pages:

1. **Return Risk Overview**
   - KPIs: Total Orders, Return Rate, Average Profit
   - Heatmap by Category & Region
2. **Product Drill-down**
   - Table with conditional formatting for high-return-risk products
3. **Interactive Filters**
   - Category, Region, Date, Payment Mode

---

## 📦 Deliverables
| Deliverable               | Format       |
|---------------------------|--------------|
| Cleaned Dataset           | `.csv`       |
| Python Prediction Code    | `.ipynb`     |
| High-Risk Product List    | `.csv`       |
| Power BI Dashboard        | `.pbix`      |
| Final Report              | `.pdf`       |

---

## ✅ Conclusion
This project provided a full pipeline for return rate analysis:
- Identified high-return categories and geographies
- Built a prediction model to flag high-risk products
- Designed a Power BI dashboard for ongoing monitoring

---

## 🔮 Next Steps
- Use advanced models like XGBoost or Random Forest
- Analyze seasonal trends in returns
- Run A/B tests to reduce return rates with policy or packaging changes

---

## 📁 Repository Structure
