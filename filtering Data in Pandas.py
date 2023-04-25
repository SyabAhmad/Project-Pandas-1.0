import pandas as pd
print("Filtering Data in Pandas")
## Filtering Data in Pandas
### there are 3 types of filtration in pandas
#### 💻 Boolean
#### 💻 Query like SQL
#### 💻 Row based on specific Values

### Boolean

data = pd.DataFrame({"Names": ["syed", "syab", "ahmad", "shah"], "Age": [21, 23, 25, 29], "Gender": ["male", "male", "male", "male"]})

print(data)
print(data["Names"])

#### Boolean format to filter Data (Conditions)
print(data[data["Age"] > 23])

#### Query selection filtration of Data
print(data.query("Gender == 'male'"))

print(data.query("Names == 'Syab'"))
print(data.query("Names == 'syab'"))

#### filtration of Row by specific Value
print(data[data["Names"].isin(["syed", "syab"])])