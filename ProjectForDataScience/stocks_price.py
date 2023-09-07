import yfinance as yf
import pandas as pd
import requests
import matplotlib.pyplot as plt

amd = yf.Ticker("AAPL")
url = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/data/amd.json'

try:
    # Send an HTTP GET request to the URL
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:

        # Parse the JSON data from the response content
        amd_info = response.json()
    
    else:
        print(f'Failed to fetch data. Status code: {response.status_code}')

except Exception as e:
    print(f'An error occurred: {str(e)}')

print('The country is ' + amd_info['country'])
print('The sector is ' + amd_info['sector'])

amd_share_price_data = amd.history(period="max")
print(amd_share_price_data.head())

amd_share_price_data.reset_index(inplace=True)

amd_share_price_data.plot(x="Date", y="Open")
plt.show()

amd.dividends.plot()

plt.show()