import pandas as pd

products= pd.read_csv(r"C:\Users\user1\PycharmProjects\MilestoneProject\data\products.csv")
customers= pd.read_csv(r"C:\Users\user1\PycharmProjects\MilestoneProject\data\customers.csv")
orders= pd.read_csv(r"C:\Users\user1\PycharmProjects\MilestoneProject\data\orders.csv")

orders_products= orders.merge(products, on= "ProductID", how="left")
full_df= orders_products.merge(customers, on= "CustomerID", how="left")

full_df["TotalPrice"]= full_df["Quantity"]* full_df["Price"]

full_df["OrderDate"]= pd.to_datetime(full_df["OrderDate"])
full_df["OrderMonth"]= full_df["OrderDate"].dt.month

full_df.to_csv("processed_order.csv", index=False)
print("ETL completed. processed_order.csv created")

