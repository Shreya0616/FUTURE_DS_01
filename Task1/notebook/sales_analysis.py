df["Order Date"] = pd.to_datetime(df["Order Date"])

monthly_sales = df.groupby(df["Order Date"].dt.to_period("M"))["Sales"].sum()
print(monthly_sales)

category_profit = df.groupby("Category")["Profit"].sum()
print(category_profit)

top_profit_products = df.groupby("Product Name")["Profit"].sum().sort_values(ascending=False).head(10)
print(top_profit_products)
