import pandas as pd

from scipy import misc
from mpl_toolkits.mplot3d import Axes3D
import matplotlib
import matplotlib.pyplot as plt

# Look pretty...
# matplotlib.style.use('ggplot')
plt.style.use('ggplot')


#
# TODO: Start by creating a regular old, plain, "vanilla"
# python list. You can call it 'samples'.
#
samples = []

#
# TODO: Write a for-loop that iterates over the images in the
# Module4/Datasets/ALOI/32/ folder, appending each of them to
# your list. Each .PNG image should first be loaded into a
# temporary NDArray, just as shown in the Feature
# Representation reading.
#
# Optional: Resample the image down by a factor of two if you
# have a slower computer. You can also convert the image from
# 0-255  to  0.0-1.0  if you'd like, but that will have no
# effect on the algorithm's results.
import os
import glob
for image_file in glob.glob('Datasets/ALOI/32/*.png'):
    img = misc.imread(image_file)
    samples.append((img[::2, ::2]/255.0).reshape(-1))

#
# TODO: Once you're done answering the first three questions,
# right before you converted your list to a dataframe, add in
# additional code which also appends to your list the images
# in the Module4/Datasets/ALOI/32_i directory. Re-run your
# assignment and answer the final question below.
#
for image_file in glob.glob('Datasets/ALOI/32i/*.png'):
    img = misc.imread(image_file)
    samples.append((img[::2, ::2] / 255.0).reshape(-1))


#
# TODO: Convert the list to a dataframe
#
df = pd.DataFrame(samples)

#
# TODO: Implement Isomap here. Reduce the dataframe df down
# to three components, using K=6 for your neighborhood size
#
from sklearn import manifold
iso = manifold.Isomap(n_neighbors=6, n_components=3)
iso.fit(df)
T = iso.transform(df)


#
# TODO: Create a 2D Scatter plot to graph your manifold. You
# can use either 'o' or '.' as your marker. Graph the first two
# isomap components
#
fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_title("IsoMap")
ax.set_xlabel('Component1')
ax.set_ylabel('Component2')
ax.scatter(T[:,0],T[:,1], marker='.', alpha=0.7)

#
# TODO: Create a 3D Scatter plot to graph your manifold. You
# can use either 'o' or '.' as your marker:
#
# Render IsoMap
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_title('IsoMap 3D')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.scatter(T[:,0], T[:,1], T[:,2], c='green', marker='o', alpha=0.75)

plt.show()

