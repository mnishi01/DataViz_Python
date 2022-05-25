import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

df_used_cars = pd.read_csv("G:/My Drive/Training/Data Visualization/Bar Chart/bar_chart_data.csv")

plt.figure(figsize = (9, 6))
plt.bar(x = df_used_cars["Brand"], height = df_used_cars["Cars Listings"], color = "midnightblue")
plt.xticks(rotation = 45, fontsize = 13)
plt.yticks(fontsize = 13)
plt.title("Cars Listings by Brand", fontsize = 16, fontweight = "bold")
plt.ylabel("Number of Listings", fontsize = 13)
plt.show()

