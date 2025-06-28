#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.tsa.statespace.sarimax import SARIMAX

# Load and prepare data
df = pd.read_csv("sales_data.csv", parse_dates=['Order_Date'])
df['Revenue'] = df['Quantity'] * df['Unit_Price']
df.dropna(inplace=True)

# KPIs
monthly_sales = df.groupby(pd.Grouper(key='Order_Date', freq='M')).agg({'Revenue': 'sum'}).reset_index()
top_customers = df.groupby('Customer_Name')['Revenue'].sum().nlargest(5)
top_products = df.groupby('Product')['Revenue'].sum().nlargest(5)

# Plot monthly revenue
sns.set(style="whitegrid")
plt.figure(figsize=(12, 6))
sns.lineplot(data=monthly_sales, x='Order_Date', y='Revenue', marker='o')
plt.title("Monthly Sales Revenue")
plt.ylabel("Revenue")
plt.xlabel("Month")
plt.tight_layout()
plt.savefig("monthly_revenue.png")
plt.close()

# Time series forecasting (12 months)
sales_ts = monthly_sales.set_index('Order_Date')['Revenue']
model = SARIMAX(sales_ts, order=(1,1,1), seasonal_order=(1,1,1,12))
results = model.fit(disp=False)

forecast = results.predict(start=len(sales_ts), end=len(sales_ts)+11, dynamic=False)
forecast.index = pd.date_range(sales_ts.index[-1] + pd.offsets.MonthBegin(1), periods=12, freq='MS')
forecast_df = pd.DataFrame({'Forecasted_Revenue': forecast})
forecast_df.to_csv("forecast.csv")

# Print insights
print("\n📊 Top Customers:")
print(top_customers)
print("\n📦 Top Products:")
print(top_products)
print("\n📈 Forecast saved to forecast.csv")
print("📊 Monthly revenue chart saved as monthly_revenue.png")


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




