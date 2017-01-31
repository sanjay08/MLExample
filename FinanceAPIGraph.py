import pandas as pd 
import matplotlib 
import matplotlib.pyplot as plt 

from matplotlib import style
import datetime 
import pandas.io.data as web


#Start date  and end date to fetch data
start=datetime.datetime(2016,1,1)
end=datetime.datetime(2017,1,31)

#data frame
df=web.DataReader("GOOG","google",start,end)

#prints head 5 rows
df.head()

#what matplotlib style are present in styles
print(style.available)

#dataframe with a paticular coloumn name
style.use('ggplot')
df['Open'].plot()
plt.show()

#dataframe without coloumn
df.plot()
plt.show()

#Using Histogram with a list of 36 Patch objects as bins
plt.hist(df.Volume,bins=36)