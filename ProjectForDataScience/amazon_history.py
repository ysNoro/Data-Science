import requests
import pandas as pd
from bs4 import BeautifulSoup

url = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/amazon_data_webpage.html'

# Get the data
data = requests.get(url).text

# Parse the data
soup = BeautifulSoup(data, 'html5lib')

# Use pandas to read the html
read_pandas_html = pd.read_html(url)

# Because there is only 1 table, we take the first entry
amazon_df = read_pandas_html[0]
amazon_df.head()

print(amazon_df)