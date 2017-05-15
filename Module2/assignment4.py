import pandas as pd


# TODO: Load up the table, and extract the dataset
# out of it. If you're having issues with this, look
# carefully at the sample code provided in the reading
# read_html returns a series of DataFrame object, thus choosing the first DataFrame here
df = pd.read_html('http://www.espn.com/nhl/statistics/player/_/stat/points/sort/points/year/2015/seasontype/2')[0]

# TODO: Rename the columns so that they are similar to the
# column definitions provided to you on the website.
# Be careful and don't accidentially use any names twice.
#
df.columns = df.iloc[1]  # selecting the 1th row and setting it as the column
df = df[2:]  # removing the first two rows including the 1th row as it's redundant with column
df.columns.name = None  # https://stackoverflow.com/questions/43854043/reindexing-pandas-dataframe
df.reset_index(drop=True, inplace=True)  # resetting index numbering so that it starts with 0


# TODO: Get rid of any row that has at least 4 NANs in it,
# e.g. that do not contain player points statistics
#
df.dropna(axis=0, thresh=4, inplace=True)
df.reset_index(drop=True, inplace=True)  # resetting index with drop=True


# TODO: At this point, look through your dataset by printing
# it. There probably still are some erroneous rows in there.
# What indexing command(s) can you use to select all rows
# EXCEPT those rows?
df = df[(df.RK != 'RK') & (df.RK.notnull())]

# TODO: Get rid of the 'RK' column
#
df.drop('RK', axis=1, inplace=True)  # removing RK column. Here axis=1 is for column


# TODO: Ensure there are no holes in your index by resetting
# it. By the way, don't store the original index
#
df.reset_index(drop=True, inplace=True)


# TODO: Check the data type of all columns, and ensure those
# that should be numeric are numeric
#
print(df.dtypes)
df_temp1 = df.ix[:, ['PLAYER', 'TEAM']]
df_temp2 = df.ix[:, 2:]
df_temp2 = df_temp2.apply(pd.to_numeric, errors='ignore')
df = pd.concat([df_temp1, df_temp2], axis=1)

# TODO: Your dataframe is now ready! Use the appropriate 
# commands to answer the questions on the course lab page.
#
print(df.shape)
print('========= Unique PCT values ===========')
print(df.PCT.unique())
print('======== Adding GP values in indices 15 and 16 ===================')



