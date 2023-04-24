import pandas as pd
# to import data from CSV file which means "Comma Separated Values" we will use read_csv(and file name and destination)
#### index_col = 1, means dont show the default index
data = pd.read_csv("data/customers-100.csv", index_col=1, parse_dates=False)
print(data)
#### Now to display some specific column to user
data = pd.DataFrame(data)

print(data["Website"])
print(data["Index"])
print(data["Company"])
print(data["Email"])

### related Function of DataFrame
#### Describe
#### info
#### min
#### max etc

print(data.max())
print(data.max())
print(data.describe())
print(data.info)