import pandas as pd
import os

#Load processed orders
df = pd.read_csv("processed_orders.csv")
#  Ensure reports folder exists
os.makedirs("reports", exist_ok=True)

#Total revenue by product category
revenue_by_category = df.groupby("Category")["TotalPrice"].sum().reset_index()
revenue_by_category = revenue_by_category.sort_values(by="TotalPrice", ascending=False)
revenue_by_category.to_csv("reports/revenue_by_category.csv", index=False)
print(" Revenue by category saved to reports/revenue_by_category.csv")


# Top 3 customers by spending
customer_spending = df.groupby(["CustomerID", "Name"])["TotalPrice"].sum().reset_index()
top_customers = customer_spending.sort_values(by="TotalPrice", ascending=False).head(3)
top_customers.to_csv("reports/top_3_customers.csv", index=False)
print("Top 3 customers saved to reports/top_3_customers.csv")


#  Monthly revenue trends
df["OrderDate"] = pd.to_datetime(df["OrderDate"])
df["OrderMonth"] = df["OrderDate"].dt.to_period('M')
monthly_revenue = df.groupby("OrderMonth")["TotalPrice"].sum().reset_index()
monthly_revenue.to_csv("reports/monthly_revenue.csv", index=False)
print("Monthly revenue trends saved to reports/monthly_revenue.csv")