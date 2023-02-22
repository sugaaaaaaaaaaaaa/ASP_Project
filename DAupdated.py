import pandas as pd
import plotly.express as px

df = pd.read_excel("Project_File.xlsx", index_col=0)
df.head()
print(df.shape)
df.columns = df.columns.str.strip()
df.index = df.index.str.strip()
print(df.columns)

# Choose Asia as the region
df = df[['Brunei Darussalam', 'Indonesia', 'Malaysia', 'Philippines', 'Thailand',
       'Viet Nam', 'Myanmar', 'Japan', 'Hong Kong', 'China', 'Taiwan',
       'Korea, Republic Of', 'India', 'Pakistan', 'Sri Lanka', 'Saudi Arabia',
       'Kuwait', 'UAE']]
print(df.shape)
df = df[:"1987 Dec"]
print(df.shape)
print(df)
# Removing all NA and replacing with 0
df = df.replace(' na ', 0)
# Converting all columns to integers
df = df.apply(pd.to_numeric)
print(df.info())

print(df.isna().sum())

fig = px.line(df, x=df.index, y=df.columns)
fig.show()
# Total travellers from each country in given 10 years
df.sum(axis=0).sort_values(ascending= False)
# Top 3 countries in given 10 years
df.sum(axis=0).sort_values(ascending= False)[:3]

import unittest

class DA(unittest.TestCase):

       def test_upper       (self):
              self.assertEqual('foo'.upper(), 'FOO')

       def test_isupper(self):
              self.assertTrue('FOO'.isupper())
              self.assertFalse('Foo'.isupper())

if __name__=='__main__':
       unittest.main()





