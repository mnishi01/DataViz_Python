import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

df_spx_ftse_00_10 = pd.read_csv("G:/My Drive/Training/Data Visualization/Line Chart/line_chart_data.csv")

df_spx_ftse_00_10["new_date"] = pd.to_datetime(df_spx_ftse_00_10["Date"])

labels = ["S&P 500", "FTSE 100"]

plt.figure(figsize=(20,8))
plt.plot(df_spx_ftse_00_10["new_date"],df_spx_ftse_00_10["GSPC500"])
plt.plot(df_spx_ftse_00_10["new_date"],df_spx_ftse_00_10["FTSE100"])
plt.title("S&P vs FTSE Returns (2000 -2010)", fontsize = 14, fontweight = "bold")
plt.ylabel("Returns")
plt.xlabel("Date")
plt.legend(labels = labels, fontsize = "large")
plt.show()
