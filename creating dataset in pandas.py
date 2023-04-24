print("Creating Datasets in Pandas")
import pandas as pd
print("Printing data set with out custom index")
dataset1 = pd.Series([1,2,3,4,5,6,7,8,9])
print(dataset1)
print("==========================\n\n")

# if you want to give index to each item in the Series then you can do that as below
dataset2 = pd.Series([1,2,3,4,5,6,7,8,9], index=['a','b','c','d','e','f','g','h', 'i'])
print("Printing data set with out custom index")
print(dataset2)
print("==========================\n\n")

# this was the creation of Series Dataset

# Now we will create a DataFrame data set

dataset3 = pd.DataFrame([[dataset1], [dataset2],])
# the above statement will create a DataFrame from the very above Series datasets
# and will show them below
print(dataset3)

# Now we will create a DataFrame with new Values below

dataset4 = pd.DataFrame([['ages', "names", "gender"], [21, "Syab", "male"], [13, "zeyad", "male"],[15, "rayan", "male"], [45, "marya", "female"]], columns=['ages', "names", "gender"])

# da first [] contains values should be the names of the columns in the DataFrame
# but remember to indecate at the end that these are the column head values like this
# columns=['ages', "names", "gender"] at the end of the data set
# and the other [] values should be the values of the columns in the DataFrame
print(dataset4)

# Now to filtering the data
# if we want to show only the names column of the Dataframes
# we can do that by just typing...
print(dataset4["names"])
# if age then
print(dataset4["ages"])
# if gender then
print(dataset4["gender"])

# if you want to print those ages where some conditions met then
# first we will convert the ages values to numeric data type

# by doing just conversion
dataset4["ages"] = pd.to_numeric(dataset4["ages"], errors="coerce")

print(dataset4.loc[dataset4["ages"] > 18, ["ages", "names", "gender"]])


