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
plt.title("The total average sales over the last 6 months")
plt.show()

#Bar graph for current monthly sales for different items 
colors = ["red", "green", "blue", "yellow", "magenta", "cyan","black", "gray", "silver", "lightblue", "maroon", "olive", "darkgreen", "purple", "teal", "navy","orange", "brown", "pink", "gold", "greenyellow", "skyblue", "darkblue", "darkcyan", "lime", "indigo", "violet", "crimson","salmon", "turquoise"]
x = itemdf["Item Desc"]
y = itemdf["Current Monthly Sales"]
plt.bar(x,y, color = colors)
plt.title("Current Monthly Sales for all items")
plt.xticks(rotation = 45)
plt.show()

#Bar graph for the total current inventory per franchise
colours = ['red', 'green', 'blue', 'purple']
franchisestock =  itemdf.groupby("Franchise")["Current Stock"].sum()
x = frandf["franchise_desc"]
y = franchisestock
plt.bar(x, y, color = colours)
plt.title("Total current inventory per franchise")
plt.show()

#Bar graph for sales per item over last 6 months
counter = 0
x = ["Month 6","Month 5","Month 4","Month 3","Month 2","Month 1"]
fig, axis = plt.subplots(5,6, sharex = True )
axis = axis.flatten()
fig.suptitle("Sales over the last 6 months for each item")
plt.subplots_adjust(hspace = 0.5)
for item in itemdf["Item Desc"]:
    ax = axis[counter]
    months6 = itemdf.loc[itemdf["Item Desc"] == item, ["Last Month Sales - 5","Last Month Sales - 4","Last Month Sales - 3","Last Month Sales - 2","Last Month Sales - 1","Last Month Sales"]].values[0]
    ax.plot(x, months6, color = colors[counter])
    ax.set_title(item)
    counter = counter + 1
    ax.tick_params(rotation = 90)
plt.show()
