import os
import pandas as pd


df = pd.read_csv("coinmarketcap_dataset_reorder.csv")
# print(df)

if not os.path.exists("sumstat_files"):
	os.mkdir("sumstat_files")

#summary statistics
mean1 = df['price'].mean()
mean2 = df['marketcap'].mean()
min1 = df['price'].min()
min2 = df['marketcap'].min()
max1 = df['price'].max()
max2 = df['marketcap'].max()
median1 = df['price'].median()
median2 = df['marketcap'].median()
var1 = df['price'].var()
var2 = df['marketcap'].var()
std1 = df['price'].std()
std2 = df['marketcap'].std()

# grouping by name 
groupby_median1 = df.groupby(['name']).median()
groupby_std1 = df.groupby(['name']).std()

print('Mean Price: ' + str(mean1))
print('Max Price: ' + str(max1))
print('Min Price: ' + str(min1))
print('Median Price: ' + str(median1))
print('Std of Prices: ' + str(std1))
print('Var of Prices: ' + str(var1))
print('Mean Marketcap: ' + str(mean2))
print('Max Marketcap: ' + str(max2))
print('Min Marketcap: ' + str(min2))
print('Median Marketcap: ' + str(median2))
print('Std of Marketcaps: ' + str(std2))
print('Var of Marketcaps: ' + str(var2))

print ('Sum of values, grouped by coin: ' + str(groupby_median1))
print ('Standard Deviance of values, grouped by coin: ' + str(groupby_std1))

df.to_csv("sumstat_files/coinmarketcap_sumstat.csv")