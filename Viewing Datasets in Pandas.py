import pandas as pd
dataset4 = pd.DataFrame([['ages', "names", "gender"], [21, "Syab", "male"], [13, "zeyad", "male"],[15, "rayan", "male"], [45, "marya", "female"]], columns=['ages', "names", "gender"])

# if we want to show all the data set
print(dataset4)
# if want to display name only
print(dataset4["names"])
# if ages then
print(dataset4["ages"])
# if gender then
print(dataset4["gender"])
# if two columns multiple then
print(dataset4[["names", "ages"]])

# filtration using loc method
dataset4["ages"] = pd.to_numeric(dataset4["ages"], errors="coerce")
print(dataset4.loc[dataset4["ages"] > 18, ["ages", "names", "gender"]])