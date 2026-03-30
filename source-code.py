# ================================
# 🔥 DATA CLEANING + ANALYSIS
# ================================

import pandas as pd
import matplotlib.pyplot as plt

# Clean column names
df.columns = df.columns.str.lower().str.replace(" ", "_")

# Convert dates
df["order_date"] = pd.to_datetime(df["order_date"])
df["ship_date"] = pd.to_datetime(df["ship_date"])

# Check missing values
print("Missing Values:\n", df.isnull().sum())

# Remove duplicates
df.drop_duplicates(inplace=True)

# Feature engineering
df["order_year"] = df["order_date"].dt.year
df["order_month"] = df["order_date"].dt.month
df["sales_per_quantity"] = df["sales"] / df["quantity"]

# ================================
# 📊 ANALYSIS
# ================================

# Total Sales
print("\n Total Sales:", df["sales"].sum())

# Category-wise sales
category_sales = df.groupby("category")["sales"].sum()
print("\n Category Sales:\n", category_sales)

# Region-wise sales
region_sales = df.groupby("region")["sales"].sum()
print("\n Region Sales:\n", region_sales)

# ================================
#VISUALIZATION
# ================================

# Yearly sales trend
plt.figure()
df.groupby("order_year")["sales"].sum().plot()
plt.title("Yearly Sales Trend")
plt.show()

# Category-wise sales
plt.figure()
category_sales.plot(kind="bar")
plt.title("Sales by Category")
plt.show()

# Region-wise sales
plt.figure()
region_sales.plot(kind="pie", autopct="%1.1f%%")
plt.title("Sales by Region")
plt.ylabel("")
plt.show()

print("\n Project Completed Successfully!")
