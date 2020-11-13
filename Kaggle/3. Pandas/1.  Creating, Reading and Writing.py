# There are two core objects in pandas: the DataFrame and the Series.

# A DataFrame is a table. It contains an array of individual entries, each of which has a certain value.
# Each entry corresponds to a row (or record) and a column.
            pd.DataFrame({'Bob': ['I liked it.', 'It was awful.'],
                          'Sue': ['Pretty good.', 'Bland.']},
                         index=['Product A', 'Product B'])

# A Series, by contrast, is a sequence of data values. If a DataFrame is a table, a Series is a list.
# And in fact you can create one with nothing more than a list:
# A Series is, in essence, a single column of a DataFrame. So you can assign column values to the
# Series the same way as before, using an index parameter. However, a Series does not have a column
# name, it only has one overall name:
            pd.Series([30, 35, 40], index=['2015 Sales', '2016 Sales', '2017 Sales'], name='Product A')\

# We'll use the pd.read_csv() function to read the data into a DataFrame. This goes thusly:
            wine_reviews = pd.read_csv("../input/wine-reviews/winemag-data-130k-v2.csv"

# We can use the shape attribute to check how large the resulting DataFrame is:
            wine_reviews.shape

# We can examine the contents of the resultant DataFrame using the head() command, which grabs the first five rows:
            wine_reviews.head()

# The pd.read_csv() function is well-endowed, with over 30 optional parameters you can specify.
# For example, you can see in this dataset that the CSV file has a built-in index,
# which pandas did not pick up on automatically. To make pandas use that column for the index
# (instead of creating a new one from scratch), we can specify an index_col.
            wine_reviews = pd.read_csv("../input/wine-reviews/winemag-data-130k-v2.csv", index_col=0)
            wine_reviews.head()