import pandas as pd

# Load dataset
df = pd.read_csv("data/sales_data.csv")

# --- KPI Calculations ---

# Conversion Rate (Visitors → Customers)
df["Conversion_Rate"] = df["Customers"] / df["Visitors"]

# Cost Per Acquisition (CAC)
df["CAC"] = df["Marketing_Spend"] / df["Customers"]

# Average Order Value (AOV)
df["AOV"] = df["Revenue"] / df["Customers"]

# Monthly Growth Rate (Revenue growth)
df["Revenue_Growth"] = df["Revenue"].pct_change()

print("=== KPI Dashboard ===")
print(df)
