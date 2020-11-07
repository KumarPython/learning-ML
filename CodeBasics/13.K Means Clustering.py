from sklearn.cluster import KMeans
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
df=pd.read_csv('income.csv')

#We want to divide into 3 clusters
km=KMeans(n_clusters=3)

y_pre=km.fit_predict(df[['Age','Income($)']])

#Feature Scaling
scalar=MinMaxScaler()
scalar.fit(df[['Income($)']])
df['Income($)']=scalar.transform(df['Income($)'])
