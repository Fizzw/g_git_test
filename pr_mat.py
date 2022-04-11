import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression
"""
cars = pd.read_csv('cars.csv',nrows=None)
print(cars.head())

x=cars['speed']
y=cars['dist']

lr = LinearRegression()

lr.fit(x.values.reshape(-1,1),y)
print('w=',lr.coef_,'b=',lr.intercept_)
print('speed=19 dist=',lr.predict([[19]]))

plt.xlabel("Speed")
plt.ylabel("Distance")
plt.plot(x,y,'o')
plt.plot(x,lr.predict(x.values.reshape(-1,1)))
plt.show()
"""
font1 ={
        'family':'serif',
        'color': 'b',
        'weight': 'bold',
        'size':14}
font2 = {
         'family':'fantasy',
         'color':'deeppink',
         'weight':'normal',
         'size':'xx-large'}
plt.plot([1,2,3,4],[2,3,5,10],label='price')
plt.plot([1,2,3,4],[3,5,7,9],label='demind')
plt.xlabel("xline",labelpad=(10),fontdict=font1,loc='left')
plt.ylabel("yline",labelpad=(10),fontdict=font2,loc='bottom')
plt.legend(loc='best',ncol=2,fontsize = 14,frameon = True,shadow=True)
plt.show()