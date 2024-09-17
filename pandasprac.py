#Q - what is pandas 
#A - Pandas is Python library which is used for working with differenct data sets for anyalizing, cleaning, exploring, manipulating, representing.
#Q - why it is used in data science 
#A - to solve complex data in short data, show statics, convert big data to small dataset
#Q - How to use pandas using VSCODE
#A - Go to terminal and use command pip install pandas
#Q - Do we have any prerequest for pandas
#A - yes, we need numpy, matplotlib and some knowledge about files handing, dataset in python
#Q - which package is used for pandas
#A - import pandas as pd
#Q - How to create dataframe using dictionary/list/tuples in python with pandas
#A - 
import pandas as pd


mydictDataSet = {
    'technologies' : ['Python', 'Java', 'C', 'mysql'],
    'jobs':[10000000, 1500000, 200000, 390000]
}

#create dataframe from dict in pandas
jobwithtech = pd.DataFrame(mydictDataSet)

#print(jobwithtech)

#Q - Create dataframe using numpy array arange function in pandas
import numpy as np

myDataFrame = pd.DataFrame(data = np.arange(0,10).reshape(2,5), index =["r1", "r2"], columns= ["c1", "c2", "c3", "c4", "c5"])
#print(myDataFrame)

#Q - what is the main function in pandas, and why we used head() and tail() function
myDataFrame = pd.DataFrame(data = np.arange(0,100).reshape(50,2))
print(myDataFrame.head()) #head will return top 5 rows in dataframe
print(myDataFrame.tail()) #tail will return bottom 5 rows in dataframe
print(myDataFrame.head(20)) # head with count will return top rows based on the count

#Q - how to check dataframe information, no of columns and data types, data is null or not
# myDataFrame.info()

#Q - how to check the datatype of dataframe in pandas
#print(type(myDataFrame))

#Q - how to analyze the dataframe in pandas
print(myDataFrame.describe())

#Q - how to retrive the data from dataframe based on the columns names
print(myDataFrame[0]) # it will return the single column data
print(myDataFrame[[0,1]]) #it will return the multiple columns data

#Q - what is series and how it will different from pandas dataframe.
#A - pandas in dataframe having more than one row and column but series contains only one row or one column
print(myDataFrame[0])

#Q - how to get the data from particular row index in dataframe pandas using loc function
print(myDataFrame.loc[5]) #dataframe.loc('enter the row index or name')
print(myDataFrame.loc[[5,7,11]]) #get the multiple row data

#Q - how to get the specific row and col data together in pandas dataframe
print(myDataFrame.iloc[2:6, 0:2]) #iloc will return row and col data 

#Q - How to convert dataframe into array in pandas
print(myDataFrame.values)

#Q - How to check Nan(null) value is exist in dataframe or not
myNanDataframe = pd.DataFrame(data = [[0, np.nan, 2], [2,4,6]])
print(myNanDataframe.isnull())
#Q - how to check if values repeat many time in dataframe
#A - using df.values_counts()
#print(myNanDataframe.value_counts())
#to check the unique value in columns
print(myDataFrame[0].unique())
#arithmetic operation in dataframe pandas
print(myDataFrame > 5)



