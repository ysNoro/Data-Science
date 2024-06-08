# Each column is a panda series
# To drop missing values in python can use: 

dataframes.dropna() # axis=0 drops the entire row, axis=1 drops the entire column
df.dropna(subset=["price"], axis=0, inplace = True) # The inplace makes it so the dataframe is changed, otherwise it won't be

# To replace:

mean = df["normalized-losses"].mean()
df["normalized-losses"].replace(np.nan, mean)

# Data Normalization
# Three approaches are:

# Simple Feature Scaling
x_new = x_old/x_max

# Min-Max
x_new = (x_old - x_min)/(x_max - x_min)

# Z-score
x_new = (x_old - u)/o  # u (miu) is the average of the feature, o (sigma) is the standard deviation

# Binning is to divide the data into different bins (like Low, Medium and High for a price for example)
# To do this in three different bins we can do easily in Python:

bins = np.linspace(min(df["price"]), max(df["price"]), 4) # We get 4 "separator" values with this at equally spaced numbers
group_names = ["Low", "Medium", "High"]
df["price-binned"] = pd.cut(df["price"], bins, labels=group_names, include_lowest=True)

# Can use Histograms after to visualize the bins and data inside each