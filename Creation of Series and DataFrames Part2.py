import pandas as pd
import numpy as np
print("Creation of Data Frames")

data = pd.DataFrame({
    "Names": np.array(["Syab", "Fayaz", "Adeel", "Eyad", "Rehan"]),
    "Age": np.array([23, 25, 16, 13, 12]),
    "sex": np.array(["male","male","male","male","male",])
})

print(data)

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
