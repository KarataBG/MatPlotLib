import matplotlib.pyplot as plt
import numpy as np

from matplotlib import style as st
from sklearn.cluster import KMeans as km

st.use("ggplot")

x = [43, 57, 2, 3, 5, 1, 6, 423, 765, 432, 5, 23, 31, 987, 543, 413, 345]
y = [65, 43, 876, 674, 985, 45, 3, 8, 6, 987, 467, 321, 567, 90, 123, 543, 65]

print(len(x), len(y))

plt.scatter(x, y)
plt.show()
