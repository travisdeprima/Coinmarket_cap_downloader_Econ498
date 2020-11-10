from sklearn import linear_model
import pandas as pd

df = pd.read_csv('coinmarketcap_dataset.csv')
df_reorder = df[['name', 'price', 'marketcap', 'symbol', 'link', 'time']] # rearrange 
df_reorder.to_csv('coinmarketcap_dataset_reorder.csv', index=False)

dataset = pd.read_csv("coinmarketcap_dataset_reorder.csv")
print(dataset)

# target = dataset.iloc[:,0].values
target = dataset.iloc[:,1].values
print(target) 

data = dataset.iloc[:,2].values
print(data)

machine = linear_model.LinearRegression()

machine.fit(data, target) 
