import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("../data/superstore_sales.csv")

print("Dataset shape:", df.shape)
print(df.head())

df["Order Date"] = pd.to_datetime(df["Order Date"])

total_revenue = df["Sales"].sum()
print("Total Revenue:", total_revenue)

category_sales = df.groupby("Category")["Sales"].sum().sort_values(ascending=False)
print("\nRevenue by Category:")
print(category_sales)

egion_sales = df.groupby("Region")["Sales"].sum().sort_values(ascending=False)
print("\nRevenue by Region:")
print(region_sales)

top_products = df.groupby("Product Name")["Sales"].sum().sort_values(ascending=False).head(10)
print("\nTop 10 Products by Revenue:")
print(top_products)

monthly_sales = df.groupby(df["Order Date"].dt.to_period("M"))["Sales"].sum()
print("\nMonthly Revenue Trend:")
print(monthly_sales)

category_profit = df.groupby("Category")["Profit"].sum().sort_values(ascending=False)
print("\nProfit by Category:")
print(category_profit)

monthly_sales.plot(figsize=(10,5))
plt.title("Monthly Revenue Trend")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
