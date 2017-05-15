import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

from pandas.tools.plotting import parallel_coordinates

# Look pretty...
# matplotlib.style.use('ggplot')
plt.style.use('ggplot')


#
# TODO: Load up the Seeds Dataset into a Dataframe
# It's located at 'Datasets/wheat.data'
# 
seed_dataset = pd.read_csv('Datasets/wheat.data', index_col=0)
print(seed_dataset.head())


#
# TODO: Drop the 'id' feature, if you included it as a feature
# (Hint: You shouldn't have)
# Also get rid of the 'area' and 'perimeter' features
#
seed_dataset = seed_dataset.drop(labels=['area', 'perimeter'], axis=1)
print(seed_dataset.head())

#
# TODO: Plot a parallel coordinates chart grouped by
# the 'wheat_type' feature. Be sure to set the optional
# display parameter alpha to 0.4
#
# Parallel Coordinates Start Here:
plt.figure()
parallel_coordinates(seed_dataset, 'wheat_type')


plt.show()


