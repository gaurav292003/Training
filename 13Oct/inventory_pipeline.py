import pandas as pd
from datetime import datetime

# Step 1: Extract data from inventory.csv
df = pd.read_csv('inventory.csv')

# Step 2: Transform data
# Add RestockNeeded column
df['RestockNeeded'] = df.apply(
    lambda row: 'Yes' if row['Quantity'] < row['ReorderLevel'] else 'No',
    axis=1
)

# Calculate TotalValue column
df['TotalValue'] = df['Quantity'] * df['PricePerUnit']

# Step 3: Load the final dataframe into restock_report.csv
df.to_csv('restock_report.csv', index=False)

# Step 4: Print completion message with timestamp
timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
print(f'Inventory pipeline completed at {timestamp}')
