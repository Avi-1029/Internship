import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression

itemdf = pd.read_csv(r"C:\Users\Biju\Desktop\Jetlearn\Data Science\Internship\item_master.csv")
itemdf.info()

frandf = pd.read_csv(r"C:\Users\Biju\Desktop\Jetlearn\Data Science\Internship\franchise_master.csv")
frandf.info()

#Calculating the average monthly sales over the last 6 months:
itemdf["Avg Monthly Sales"] = itemdf[["Last Month Sales", "Last Month Sales - 1","Last Month Sales - 2","Last Month Sales - 3","Last Month Sales - 4","Last Month Sales - 5"]].sum(axis = 1)/6
print(itemdf.head(10))

#Calculating the demand during lead time:
lead_demand = []
for i in itemdf.index:
    fcode = itemdf.loc[i, "Franchise"]
    lead_time = frandf.loc[frandf["franchise_code"] == fcode , "lead_time_month"].values
    sales = itemdf.loc[i, "Avg Monthly Sales"]
    demand = sales*lead_time
    lead_demand.append(demand[0])
itemdf["Lead_time_demand"] = lead_demand

#Calculating suggested orders:
safetystock = []
for i in itemdf.index:
    fcode = itemdf.loc[i, "Franchise"]
    ss = frandf.loc[frandf["franchise_code"] == fcode, "safety_stock"].values
    safetystock.append(ss[0])
safetystock = pd.Series(safetystock)

itemdf["Suggested_order"] = np.ceil((itemdf["Lead_time_demand"] + safetystock) - (itemdf["Current Stock"] + itemdf["Backorder Qty"]))
print(itemdf.head())
#itemdf.to_csv("Item_master_new.csv")

#Prediction model
#Selecting features and target
x = itemdf[["Lead_time_demand", "Current Stock", "Backorder Qty"]]
x["Safety Stock"] = safetystock
y = itemdf["Suggested_order"]

#Building model
model = LinearRegression()
model.fit(x,y)
#bob = np.ceil(model.predict(x))
#from sklearn.metrics import root_mean_squared_error
#error = root_mean_squared_error(y, bob)
#print(error)

Lead_time= int(input("Enter the lead time: "))
avgmonthsale = float(input("Enter the average monthly sales: "))
inputsafetystock = int(input("Enter the safety stock: "))
backorder = int(input("Enter the Backorder quantity: "))
currentstock = int(input("Enter the current stock: "))

sugordpred = model.predict([[Lead_time*avgmonthsale, currentstock, backorder, inputsafetystock]])
final = np.ceil(sugordpred)[0]
print("Your suggested order is: ", final)
