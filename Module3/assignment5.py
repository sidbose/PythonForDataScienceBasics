import pandas as pd
import matplotlib.pyplot as plt
from pandas.tools.plotting import andrews_curves

plt.style.use('ggplot')

seed_dataset = pd.read_csv('Datasets/wheat.data', index_col=0)
print(seed_dataset.head())


# Andrews Curves Start Here:
plt.figure()
andrews_curves(seed_dataset, 'wheat_type')

plt.show()

