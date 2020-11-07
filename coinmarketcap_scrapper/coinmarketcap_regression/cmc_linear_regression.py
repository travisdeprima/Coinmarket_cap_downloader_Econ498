from sklearn import linear_model
import pandas

dataset = pandas.read_csv("regression_dataset.csv")
# print(dataset)

# target = dataset.iloc[:,0].values
target = dataset.iloc[:,1].values
print(target)

data = dataset.iloc[:,3:9].values
print(data)

machine = linear_model.LinearRegression()

machine.fit(data, target)

new_data = [
	[-0.44,-0.29,0.51,0.92,-0.012,0],
	[1,-0.55,0.55,1.3,-0.011,1],
	[2,-0.53,0.9,0.36,-0.0123,0],
	[2.3,-0.23,0.33,0.32,-0.019,1],
	[10,-0.23,0.33,0.32,-0.019,1],
]

results = machine.predict(new_data)