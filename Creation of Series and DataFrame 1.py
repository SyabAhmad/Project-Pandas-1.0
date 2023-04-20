print("Creation of Series and DataFrame part 1")
# series is a data set having same datatype values like integer, string...
# to create series we will import panda
import pandas as pd
data = pd.Series([1,2,3,4,5,6], index=['a', 'b', 'c', 'd', 'e', 'f'])
print(data)

print(data['a'])

# update Values at specific index
data['a'] = 44
print(data)

#to print max value
print(data.max())

# ro print Min Value
print(data.min())

# describe function is used for to find basics of statistics e.g. mean std, min, count etc
print(data.describe())


