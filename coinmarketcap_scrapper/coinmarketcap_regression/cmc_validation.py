import pandas
import numpy as np
from sklearn import linear_model
from sklearn.model_selection import train_test_split 
from matplotlib import pyplot as plt
from sklearn import metrics

dataset = pandas.read_csv("coinmarketcap_dataset_reorder.csv")
# print(dataset)

target = dataset.iloc[:,1].values
# print(target)

data = dataset.iloc[:,2].values
# print(data)

data_training, data_test, target_training, target_test = train_test_split(data, target, test_size=0.25, random_state=0)

print(data.shape)
print(target.shape)

print(data_training.shape)
print(data_test.shape)

print(target_training.shape)
print(target_test.shape)

machine = linear_model.LinearRegression()
machine.fit(data_training, target_training)

results = machine.predict(data_test)

print(results)

plt.scatter(target_test, results)
plt.xlabel("target_test")
plt.ylabel("machine_predict")

plt.savefig("scatter_test.png")

print(metrics.r2_score(target_test,results))