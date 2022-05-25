import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

df_ad_expenditure = pd.read_csv("G:/My Drive/Training/Data Visualization/Regression Plot/scatter_plot_ii.csv")

sns.set(rc = {'figure.figsize': (9,6)})
sns.regplot(x = "Budget",
            y = "Sales",
            data = df_ad_expenditure,
            scatter_kws = {'color': 'k'},
            line_kws = {'color': 'red'})
plt.xlabel("Ad Expenditure in US$k")
plt.ylabel("Sales in k Units")
plt.title("Effect of Ad Expenditure on Sales", fontsize = 14, weight = "bold")
plt.show()
