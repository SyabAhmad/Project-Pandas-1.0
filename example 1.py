print("Example 1")
import pandas as pd
data = pd.read_csv("https://raw.githubusercontent.com/datagy/data/main/insurance.csv", index_col=0, parse_dates=True)

print(data.info)

print(data.describe())

print(data["bmi"])