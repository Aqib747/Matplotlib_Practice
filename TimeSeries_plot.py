import pandas as pd
from datetime import datetime, timedelta
from matplotlib import pyplot as plt
from matplotlib import dates as mpl_dates

plt.style.use('seaborn')
#plt.xkcd()

data = pd.read_csv('BitCoin.csv')


data['Date']  = pd.to_datetime(data['Date']) # make the colomn as date time then sort it if any smaller data will add in csv it will visualize in sorted order
data.sort_values("Date",inplace = True)

price_date = data['Date']
price_close = data['Close']


plt.plot_date(price_date,price_close, linestyle = 'solid')

plt.gcf().autofmt_xdate()  # gcf means get current figure and ..... and rest is auto format the x date

plt.title("BitCoins Price")
plt.xlabel('Dates')
plt.ylabel('Closeing Price')
plt.tight_layout()
plt.show()