### There are to Types of Iteration in Pandas when it comes to Row Iterations
#### iterrows()
#### itertuples()
### Let see
import pandas as pd
data = pd.DataFrame({"Names": ["syed", "syab", "ahmad", "shah"], "Age": [21, 23, 25, 29], "Gender": ["male", "male", "male", "male"]})

print(data)
print("using iterrows Method")
for index, rows in data.iterrows():
    print(rows["Names"], rows["Age"])

### 2nd Method (itertuples)

print("using itertuples Method")
for rows in data.itertuples():
    print(getattr(rows, "Names"), getattr(rows, "Age"))