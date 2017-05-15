import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

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
# TODO: Create a slice of your dataframe (call it s1)
# that only includes the 'area' and 'perimeter' features
# 
s1 = seed_dataset[['area', 'perimeter']]
print(s1.head())


#
# TODO: Create another slice of your dataframe (call it s2)
# that only includes the 'groove' and 'asymmetry' features
# 
s2 = seed_dataset[['groove', 'asymmetry']]
print(s2.head())

#
# TODO: Create a histogram plot using the first slice,
# and another histogram plot using the second slice.
# Be sure to set alpha=0.75
# 
s1.plot.hist(alpha=0.75)
s2.plot.hist(alpha=0.75)

# Display the graphs:
plt.show()

