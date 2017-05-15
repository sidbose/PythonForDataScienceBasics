import pandas as pd
import matplotlib.pyplot as plt

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
# 
# .. your code here ..


#
# TODO: Compute the correlation matrix of your dataframe
# 
print(seed_dataset.corr())


#
# TODO: Graph the correlation matrix using imshow or matshow
# 
plt.imshow(seed_dataset.corr(), cmap=plt.cm.Blues, interpolation='nearest')
plt.colorbar()
tick_marks = [i for i in range(len(seed_dataset.columns))]
plt.xticks(tick_marks, seed_dataset.columns, rotation='vertical')
plt.yticks(tick_marks, seed_dataset.columns)

plt.show()


