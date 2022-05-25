import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

df_real_estate = pd.read_csv("G:/My Drive/Training/Data Visualization/Histogram/histogram_data.csv")

sns.set_style("white")
plt.figure(figsize=(8,6))
plt.hist(df_real_estate["Price"], 
         bins = 8,
         color = "#108A99")
plt.title("Distribution of Real Estate Prices", fontsize = 14, fontweight = "bold")
plt.ylabel("Number of Properties")
plt.xlabel("Price in US$k")
sns.despine()
plt.show()
