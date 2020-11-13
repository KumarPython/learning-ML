# Native Python objects provide good ways of indexing data. Pandas carries all of these over,
# which helps make it easy to start with.
# In Python, we can access the property of an object by accessing it as an attribute. A book object,
# for example, might have a title property, which we can access by calling book.title. Columns in a
# pandas DataFrame work in much the same way.
            reviews.country

# If we have a Python dictionary, we can access its values using the indexing ([]) operator.
# We can do the same with columns in a DataFrame:
            reviews['country']

# Index-based selection
# Pandas indexing works in one of two paradigms. The first is index-based selection:
# selecting data based on its numerical position in the data. iloc follows this paradigm.
# to drill down to a single specific value, we need only use the indexing operator [] once more:
            reviews['country'][0]

# However, pandas has its own accessor operators, loc and iloc. For more advanced operations,
# these are the ones you're supposed to be using.
            reviews.iloc[0]

# Label-based selection
# The second paradigm for attribute selection is the one followed by the loc operator:
# label-based selection. In this paradigm, it's the data index value, not its position,
# which matters.
            reviews.loc[:, ['taster_name', 'taster_twitter_handle', 'points']]

# When choosing or transitioning between loc and iloc, there is one "gotcha" worth keeping in mind, which is that the two methods use slightly different indexing schemes.
# iloc uses the Python stdlib indexing scheme, where the first element of the range is included
# and the last one excluded. So 0:10 will select entries 0,...,9.
# loc, meanwhile, indexes inclusively. So 0:10 will select entries 0,...,10.

# Label-based selection derives its power from the labels in the index. Critically, the index we use
# is not immutable. We can manipulate the index in any way we see fit.
# The set_index() method can be used to do the job. Here is what happens when we set_index to the
# title field:
            reviews.set_index("title")

# Conditional selection
# So far we've been indexing various strides of data, using structural properties of the DataFrame
# itself. To do interesting things with the data, however, we often need to ask questions based on
# conditions.For example, suppose that we're interested specifically in better-than-average wines
# produced in Italy.We can start by checking if each wine is Italian or not:
            reviews.country == 'Italy'

# This result can then be used inside of loc to select the relevant data:
            reviews.loc[reviews.country == 'Italy']

# We also wanted to know which ones are better than average. Wines are reviewed on a 80-to-100 point
# scale, so this could mean wines that accrued at least 90 points.
# We can use the ampersand (&) to bring the two questions together:
            reviews.loc[(reviews.country == 'Italy') & (reviews.points >= 90)]

# Suppose we'll buy any wine that's made in Italy or which is rated above average. For this we use a pipe (|):
            reviews.loc[(reviews.country == 'Italy') | (reviews.points >= 90)]

# Pandas comes with a few built-in conditional selectors, two of which we will highlight here.
# The first is isin. isin is lets you select data whose value "is in" a list of values.
# For example, here's how we can use it to select wines only from Italy or France:
            reviews.loc[reviews.country.isin(['Italy', 'France'])]

# The second is isnull (and its companion notnull). These methods let you highlight values
# which are (or are not) empty (NaN). For example, to filter out wines lacking a price tag in the
# dataset, here's what we would do:
            reviews.loc[reviews.price.notnull()]

# Assigning data
# Going the other way, assigning data to a DataFrame is easy. You can assign either a constant value:
            reviews['critic'] = 'everyone'

# Or with an iterable of values:
            reviews['index_backwards'] = range(len(reviews), 0, -1)
