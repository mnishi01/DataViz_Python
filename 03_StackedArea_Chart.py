import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

df_fuel_engine_types = pd.read_csv("G:\My Drive\Training\Data Visualization\Stacked Area\stacked_area_chart_data.csv")

colors = ["#011638", "#7e2987", "#ef2026"]  
labels = ["Diesel", "Petrol", "Gas"]
sns.set_style("white")
plt.figure(figsize = (12, 6))
plt.stackplot(df_fuel_engine_types["Year"],
              df_fuel_engine_types["Diesel"],
              df_fuel_engine_types["Petrol"],
              df_fuel_engine_types["Gas"],
              colors = colors,
              edgecolor = 'none')
plt.xticks(df_fuel_engine_types["Year"], rotation = 45)
plt.legend(labels = labels, loc = "upper left")
plt.ylabel("Number of Cars", fontsize = 13)
plt.title("Popularity of Engine Fuel Types (1982 - 2016)", fontsize = 14, weight = "bold")
sns.despine()
plt.show()
