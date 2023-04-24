# Project-Panda


# There are two type Dataframes

```Series``` and ```DataFrames```

```Series``` are ```1D``` labeled ```homogeneously-typed``` array and 

```Dataframes``` are General ```2D``` labeled, size-mutable tabular structure with potentially ```heterogeneously-typed``` column

# Creation od series and Data Frames

# To import Panda 

```python runable
import pandas as pd

```

# To Create Series

```python runable
import pandas as pd
# will create a series of data
data = pd.Series([1,2,3,4,5,6,7,8])
# will print the data
print(data)

```

# To print type of data

```python runable
# will print the type of data objects
print(type(data))

```
# To create Dataframe

```python runable
import pandas as pd
# will create a series of data
data = pd.Dataframe(["Column1": [1,2,3,4,5,6], "Column2": [1,2,3,4,5,6]], index=['a','b', 'c', 'd', 'e', 'f'])
# will print the data
print(data)

```

# To print type of data

```python runable
# will print the type of data objects
print(type(data))

```

# To create Seriese from day 1 and day 2 only
```python runable
import pandas as pd

calories = {"day1": 420, "day2": 380, "day3": 390}

myvar = pd.Series(calories, index = ["day1", "day2"])

print(myvar)
```

# Example of Data Frame # #1
```python runable
import pandas as pd
import numpy as np
print("Creation of Data Frames")

data = pd.DataFrame({
    "Names": np.array(["Syab", "Fayaz", "Adeel", "Eyad", "Rehan"]),
    "Age": np.array([23, 25, 16, 13, 12]),
    "sex": np.array(["male","male","male","male","male",])
})

print(data)

```
# Example of Data Frame # #1 Continue
```python runable

# to print specific column
print(data["Age"])
print(data["Names"])
print(data["sex"])

# to describe and find max and min
print(data.describe())
print(data.max())
print(data.min())

# selecting subset from dataframe
data1 = data['Names']
print(data1)

```

# Creating new Column in existing Table
``` python
import pandas as pd

data = pd.DataFrame([[1,2,3,4,5,6,7,8], [9,7,6,5,4,2,1, 78]])

print(data)
data["after division of column 2 and 3"] = data[2] / data[3]
print(data)

```



### Reading from Excel File and ploting the numeric Data

This is a project that utilizes data analysis tools to extract insights from a data set. In this project, we use Python and the Pandas library to clean, process, and analyze the data. We then visualize the results using Matplotlib.

### Installation

To run this project, you need to install the following packages:

👨‍🏫 Pandas

👨‍🏫 Matplotlib

👨‍🏫 Openpyxl

To install these packages, you can use the following command in your terminal:

```pyrhon runnable
pip install pandas matplotlib openpyxl
```

If you are using PyCharm, you can also install these packages by opening the project and navigating to File > Settings > Project: [project name] > Python Interpreter. Here, you can click on the + button to add a package, and then search for and install the required packages.


### ⚠⚠ Openpyxl package Error ⚠⚠
If you encounter an error related to the Openpyxl package, make sure to install it separately before running the command above.


Once the packages are installed, you can run the project and start analyzing the data.

# example of matplotlib.pyplot

```python runable

import pandas as pd

import matplotlib.pyplot as plt

import openpyxl as sa

# we will use same csv file

# customerdata = pd.read_csv('customers-100.csv', index_col= 0, parse_dates=True)

userdata = pd.read_excel('pandaData.xlsx', index_col=0)


#customerdata = customerdata[["Phone 1", "Phone 2"]].head(5)

print(userdata)

userdata = userdata[['Age', 'Gender']]

print(userdata)

userdata.plot()

plt.title("Friends Data")

plt.ylabel("Names")

plt.xlabel("Ages")

plt.show()

```
# Matpolotlib.pyplot second example

```python runable

import pandas as pd

import matplotlib.pyplot as plt

numericData = pd.read_excel('data/numricData.xlsx', index_col=0)

print(numericData)

numericData.plot()

plt.title("Cars Data")

plt.xlabel("Names of Cars")

plt.ylabel("Values of Cars")

plt.show()

```

# Creating data sets on Python
### 💻 Series and 
### 💻 DataFrames
```python
print("Creating Datasets in Pandas")
import pandas as pd
print("Printing data set with out custom index")
dataset1 = pd.Series([1,2,3,4,5,6,7,8,9])
print(dataset1)
print("==========================\n\n")
```
#### if you want to give index to each item in the Series then you can do that as below
```python
dataset2 = pd.Series([1,2,3,4,5,6,7,8,9], index=['a','b','c','d','e','f','g','h', 'i'])
print("Printing data set with out custom index")
print(dataset2)
print("==========================\n\n")
```
#### this was the creation of Series Dataset

#### Now we will create a DataFrame data set
```python
dataset3 = pd.DataFrame([[dataset1], [dataset2],])
```
#### the above statement will create a DataFrame from the very above Series datasets, and will show them below
print(dataset3)

#### Now we will create a DataFrame with new Values below
```python
dataset4 = pd.DataFrame([['ages', "names", "gender"], [21, "Syab", "male"], [13, "zeyad", "male"],[15, "rayan", "male"], [45, "marya", "female"]], columns=['ages', "names", "gender"])
```
#### da first [] contains values should be the names of the columns in the DataFrame, but remember to indecate at the end that these are the column head values like this
#### columns=['ages', "names", "gender"] at the end of the data set, and the other [] values should be the values of the columns in the DataFrame
```python
print(dataset4)
```
#### Now to filtering the data, if we want to show only the names column of the Dataframes, we can do that by just typing...
```python
print(dataset4["names"])
```
#### if age then
```python
print(dataset4["ages"])
```
#### if gender then
```python
print(dataset4["gender"])
```
#### if you want to print those ages where some conditions met then. first we will convert the ages values to numeric data type

#### by doing just conversion
```python
dataset4["ages"] = pd.to_numeric(dataset4["ages"], errors="coerce")

print(dataset4.loc[dataset4["ages"] > 18, ["ages", "names", "gender"]])
```

## Viewing Datasets in Pandas


```python

import pandas as pd
dataset4 = pd.DataFrame([['ages', "names", "gender"], [21, "Syab", "male"], [13, "zeyad", "male"],[15, "rayan", "male"], [45, "marya", "female"]], columns=['ages', "names", "gender"])
```
#### if we want to show all the data set
```python
print(dataset4)
```
#### if want to display name only
```python
print(dataset4["names"])
```
#### if ages then
```python
print(dataset4["ages"])
```
#### if gender then
```python
print(dataset4["gender"])
```
#### if two columns multiple then
```python
print(dataset4[["names", "ages"]])
```
#### Filtration using loc method
```python
dataset4["ages"] = pd.to_numeric(dataset4["ages"], errors="coerce")
print(dataset4.loc[dataset4["ages"] > 18, ["ages", "names", "gender"]])
```
# Reading From CSV File and viewing related functions
```python
import pandas as pd
```
### To import data from CSV file which means "Comma Separated Values" we will use read_csv(and file name and destination)
#### index_col = 1, means dont show the default index
```python
data = pd.read_csv("data/customers-100.csv", index_col=1, parse_dates=False)
print(data)
```
#### Now to display some specific column to user
```python
data = pd.DataFrame(data)
```
```python
print(data["Website"])
print(data["Index"])
print(data["Company"])
print(data["Email"])
```
### Related Function of DataFrame
#### 💻 Describe
#### 💻 info
#### 💻 min
#### 💻 max etc
```python
print(data.max())
print(data.max())
print(data.describe())
print(data.info)
```