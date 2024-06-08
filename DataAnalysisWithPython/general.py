# Import dataset from https://archive.ics.uci.edu/ml/machine-learning-databases/autos/imports-85.data

import pandas as pd

url = "https://archive.ics.uci.edu/ml/machine-learning-databases/autos/imports-85.data"

df = pd.read_csv(url, header=None)

print(df.head(5))

# To access DB we use API's
# This is done by: 1- Connect, 2- SEND, 3- EXECUTE, 4- Status Check, 5- Receive OK, 6- Disconnect