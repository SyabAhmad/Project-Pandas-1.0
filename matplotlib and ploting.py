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