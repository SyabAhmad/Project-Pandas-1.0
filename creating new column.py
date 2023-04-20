import pandas as pd

data = pd.DataFrame([[1,2,3,4,5,6,7,8], [9,7,6,5,4,2,1, 78]])

print(data)
data["after division of column 2 and 3"] = data[2] / data[3]
print(data)