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
