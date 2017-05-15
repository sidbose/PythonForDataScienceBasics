import pandas as pd

# TODO: Load up the dataset
# Ensuring you set the appropriate header column names
#
attributes = ['motor', 'screw', 'pgain', 'vgain', 'class']
df = pd.read_csv('Datasets/servo.data', names=attributes)
print df.head()
print('===================================================')

# TODO: Create a slice that contains all entries
# having a vgain equal to 5. Then print the 
# length of (# of samples in) that slice:
#
print(df['vgain'].value_counts())
print('===================================================')

# TODO: Create a slice that contains all entries
# having a motor equal to E and screw equal
# to E. Then print the length of (# of
# samples in) that slice:
#
df2 = df.loc[(df.motor == 'E') & (df.screw == 'E')]
print(df2)
print(len(df2.index))
print('===================================================')


# TODO: Create a slice that contains all entries
# having a pgain equal to 4. Use one of the
# various methods of finding the mean vgain
# value for the samples in that slice. Once
# you've found it, print it:
#
df3 = df.loc[df.pgain == 4]
print(df3['vgain'].mean())


# TODO: (Bonus) See what happens when you run
# the .dtypes method on your dataframe!
