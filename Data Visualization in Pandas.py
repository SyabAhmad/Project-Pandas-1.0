import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import random as rdm
xAxis = np.array(rdm.randint(1, 10))
yAxis = np.array(rdm.randint(1, 10))

plot = pd.DataFrame([[xAxis], [yAxis]])

### Scatter is a type of graph

plt.scatter(xAxis, yAxis)
plt.show()

