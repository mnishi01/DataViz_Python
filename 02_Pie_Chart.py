import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

df_fuel_engine_type = pd.read_csv("G:\My Drive\Training\Data Visualization\Pie Chart\pie_chart_data.csv")

sns.set_palette('colorblind')

plt.figure(figsize = (10,8))
plt.pie(df_fuel_engine_type['Number of Cars'],
       labels = df_fuel_engine_type['Engine Fuel Type'].values,
       autopct = '%.2f%%',
       textprops = {'size' : 'x-large',
                    'fontweight' : 'bold',
                    'rotation' : '30',
                    'color' : 'w'})
plt.legend()
plt.title('Cars by Engine Fuel Type', fontsize = 18, fontweight = 'bold')
plt.show()

