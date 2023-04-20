import pandas as pd
import matplotlib.pyplot as plt
numericData = pd.read_excel('data/numricData.xlsx', index_col=0)
print(numericData)

numericData.plot()
plt.title("Cars Data")
plt.xlabel("Names of Cars")
plt.ylabel("Values of Cars")
plt.show()