import pandas as pd
import numpy as np
from sklearn import metrics
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import LabelEncoder 
#import matplotlib.pyplot as plt


data = pd.read_csv('datafile1.csv')
data.info()


category= ['Name','Age','Gender','Answer', 'User', 'Time']
encoder= LabelEncoder()
for i in category:  
   data[i] = encoder.fit_transform(data[i])

data. shape
feature = ['Answer']
target = ['Time']
X = data[feature]
#print(X.shape)
y = data[target]
#print(y.shape)

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state = 1)
#print(X_train.shape)
#print(X_test.shape)
#print(y_train.shape)
#print(y_test.shape)

X_train1 = X[:-100]
X_test1 = X[-100:]

# Split the targets into training/testing sets
y_train1 = y[:-100]
y_test1 = y[-100:]

logreg=LinearRegression()
logreg.fit(X,y)
a=logreg.predict(X)

pretym=mean_squared_error(y_test1, a)


print("Prediction of time: %.2f" %pretym)
# The coefficient of determination: 1 is perfect prediction
#print("Coefficient of determination: %.2f" % r2_score(y_test1, a))
# plt.hist(data['Time'],bins=10, alpha=0.5)
# plt.hist(data['Answer'], bins=10, alpha=.5, orientation='horizontal')

# fig, ax = plt.subplots()
# ax.bar(data['Time'], data['Answer'])

# plt.show()