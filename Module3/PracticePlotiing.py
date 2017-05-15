import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

plt.style.use('ggplot')  # Look Pretty

student_dataset = pd.read_csv('Datasets/students.data', index_col=0)

# Drawing histograms
# my_series = student_dataset.G3
# my_dataframe = student_dataset[['G1', 'G2', 'G3']]
# my_series.plot.hist(alpha=0.3)   # alpha is used for transparency
# my_dataframe.plot.hist(alpha=0.5)
# plt.show()

# Drawing scatter plot
# ax = student_dataset.plot.scatter(x='G1', y='G2', color='r', label='G1 vs G2')
# student_dataset.plot.scatter(x='G1', y='G3', marker='^', color='b', label='G1 vs G3', ax=ax)
# plt.title("Relationship between G1,G2 and G3")
# plt.xlabel('G1 & G2 score')
# plt.ylabel('G3 score')
# plt.legend(loc='upper left')
# plt.show()


# Drawing 3d scatter plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_xlabel('Final Grade')
ax.set_ylabel('First Grade')
ax.set_zlabel('Daily Alcohol')
ax.scatter(student_dataset.G1, student_dataset.G3, student_dataset.Dalc, c='r', marker='.')
plt.show()

