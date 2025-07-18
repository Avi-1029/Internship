import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

itemdf = pd.read_csv(r"C:\Users\Biju\Desktop\Jetlearn\Data Science\Internship\item_master.csv")
itemdf.info()

frandf = pd.read_csv(r"C:\Users\Biju\Desktop\Jetlearn\Data Science\Internship\franchise_master.csv")
frandf.info()

#Calculating the average monthly sales over the last 6 months:
itemdf["Avg Monthly Sales"] = itemdf[["Last Month Sales", "Last Month Sales - 1","Last Month Sales - 2","Last Month Sales - 3","Last Month Sales - 4","Last Month Sales - 5"]].sum(axis = 1)/6
print(itemdf.head(10))

#Calculating the demand during lead time:

lead_demand = []
for fcode, sales in itemdf[["Franchise", "Avg Monthly Sales"]]:
    demand = frandf.loc[frandf["franchise_code"] == fcode, "lead_time_month"]*sales
    lead_demand.append(demand)
print(lead_demand)