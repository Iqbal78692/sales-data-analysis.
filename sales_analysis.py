
# Sales Data Analysis
import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv('sales_data.csv')

# Calculate total sales
df['Total Sales'] = df['Units Sold'] * df['Unit Price']

# Total sales by product
product_sales = df.groupby('Product')['Total Sales'].sum()
print("Total Sales by Product:\n", product_sales)

# Total sales by region
region_sales = df.groupby('Region')['Total Sales'].sum()
print("\nTotal Sales by Region:\n", region_sales)

# Plotting
product_sales.plot(kind='bar', title='Total Sales by Product')
plt.xlabel('Product')
plt.ylabel('Sales')
plt.tight_layout()
plt.show()

region_sales.plot(kind='bar', title='Total Sales by Region', color='orange')
plt.xlabel('Region')
plt.ylabel('Sales')
plt.tight_layout()
plt.show()
