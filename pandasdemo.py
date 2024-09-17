import pandas as pd

print(pd.__version__)
#show the apple stock growth using matplotlib and pandas
import matplotlib.pyplot as plt

# df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/2014_apple_stock.csv')
# df.plot()
# plt.show()

#show the current dollar index using read json in pandas
import requests
from pandas.io.json import _json
import pandas as pd

# url = "https://api.exchangerate-api.com/v4/latest/USD"
# df = pd.read_json(url)
# print(df['rates'])

#save/write the json from dataframe in pandas
import json
# df = pd.DataFrame([1,2,3])
# df.to_json('sample.json')

#read the json data from file show in dataframe in pandas
# df = pd.read_json('sample.json')
# print(df.values)

#read and write the data in csv file using dataframe in pandas
# df = pd.DataFrame([1,2,3])
# df.to_csv('sample.csv')

# x









 