import pandas as pd
import plotly.express as px
import unittest

# Reading the file
df = pd.read_excel("Project_File.xlsx")
df.head()

print(df.shape)
df.astype("str")

# Split Year and Month
df = df.rename(columns={df.columns[0]: "Year"})
df[['Year','Month']] = df['Year'].str.split(n = 1, expand=True)

# Removal of White space
df.columns = df.columns.str.strip()
print(df.columns)

# Choose Asia as the region
df = df[['Year','Brunei Darussalam', 'Indonesia', 'Malaysia', 'Philippines', 'Thailand',
      'Viet Nam', 'Myanmar', 'Japan', 'Hong Kong', 'China', 'Taiwan',
       'Korea, Republic Of', 'India', 'Pakistan', 'Sri Lanka', 'Saudi Arabia',
       'Kuwait', 'UAE']]
print(df)

print(df.shape)
print(df)

# Filtering of Year
df = df[(df['Year'] > "1978") & (df['Year'] < "1988")]
print(df)

# Removing all NA and replacing with 0
df = df.replace(' na ', 0)
print(df)
# Converting all columns to integers
df = df.apply(pd.to_numeric)
print(df.info())
print(df.isna().sum())
print(df.info())

# Plotting of Graph
fig = px.bar(df, x=df['Year'], y=df.columns)
fig.show()

# Test Case
class DA(unittest.TestCase):

       def test_upper       (self):
              #self.assertEqual('foo'.upper(), 'FOO')

       def test_isupper(self):
              #self.assertTrue('FOO'.isupper())
              #self.assertFalse('Foo'.isupper())

if __name__=='__main__':
       #unittest.main()
