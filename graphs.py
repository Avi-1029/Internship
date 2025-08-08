import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

itemdf = pd.read_csv(r"C:\Users\Biju\Desktop\Jetlearn\Data Science\Internship\item_master_new.csv")
itemdf.info()

frandf = pd.read_csv(r"C:\Users\Biju\Desktop\Jetlearn\Data Science\Internship\franchise_master.csv")
frandf.info()

#Line plot for the total avg sales in the last 6 months: 
avg = itemdf[["Last Month Sales","Last Month Sales - 1","Last Month Sales - 2","Last Month Sales - 3","Last Month Sales - 4","Last Month Sales - 5"]].mean()
avg = avg[::-1]
plt.plot(avg.index, avg)
plt.show()

#Bar graph for current monthly sales for different items 
x = itemdf["Item Desc"]
y = itemdf["Current Monthly Sales"]
plt.bar(x,y)
plt.xticks(rotation = 45)
plt.show()

#Bar graph for the total current inventory per franchise
franchisestock =  itemdf.groupby("Franchise")["Current Stock"].sum()
x = frandf["franchise_desc"]
y = franchisestock
plt.bar(x, y)
plt.show()

#Bar graph for sales per item over last 6 months
counter = 0
fig, axis = plt.subplots(5,6, sharex = True )
y_values = []
for item in itemdf["Item Desc"]:
    y = itemdf.loc[itemdf["Item Desc"] == item, ["Last Month Sales","Last Month Sales - 1","Last Month Sales - 2","Last Month Sales - 3","Last Month Sales - 4","Last Month Sales - 5"]]
    y_values.append(y.values[0])
for row in axis:
    for ax in row:
        ax.plot(x, y_values[counter])
        counter = counter + 1
        # ax.
        # (f"Total sales over last 6 months for {item}")
    
plt.show()


