import pandas as pd
data = pd.DataFrame({"Names": ["syab", "adeel", "fayaz"], "Age":[21,16,25], "Phone Number": [123,456,789]})
print(data)


# selection of specific column
print(data["Names"])
print(data["Age"])
print(data["Phone Number"])

print(data.iloc[1,1])

