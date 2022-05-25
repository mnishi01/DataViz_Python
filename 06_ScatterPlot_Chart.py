import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

df_real_estate = pd.read_csv("G:/My Drive/Training/Data Visualization/Scatter Plot/scatter_data.csv")

plt.figure(figsize=(12,8))
scatter = plt.scatter(df_real_estate["Area (ft.)"], 
            df_real_estate["Price"],
            alpha = 0.6,
            c = df_real_estate['Building Type'],
            cmap = 'viridis')
plt.legend(*scatter.legend_elements(),
           loc = "upper left",
          title = "Building Type")
plt.title("Relationship between Area and Price of California Real Estate", 
          fontsize = 14, 
          fontweight = "bold")
plt.ylabel("Price in US$k")
plt.xlabel("Area (in sq feet)")
sns.despine()
plt.show()
