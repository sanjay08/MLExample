import pandas as pd 
import matplotlib 
import matplotlib.pyplot as plt 
from matplotlib import style
import datetime as dt 
import pandas.io.data as web

#create dateframe

start=datetime.datetime(2016,1,1)
end=datetime.datetime(2017,1,1)


#From goggle finance api fecth data
df=web.DataReader("GOOG","google",start,end)


#Head Function

df.head()


#what style are available in matplotlib
print(style.available)

style.use('seaborn-notebook')

df['Open'].plot()
plot.show()

#if you want to show close value then us<df['Close'].plot()>
