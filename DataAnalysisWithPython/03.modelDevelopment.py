# There are:
# Linear Regression - one independent variable to make a prediction
# Multiple Linear Regression - multiple independent variables to make a prediction

# LINEAR REGRESSION:
y = b0 + b1*x
# b0 is the intercept
# b1 is the slope

# In Python:
from sklearn.linear_model import LinearRegression

# Create Linear Regression object using the constructor
lm = LinearRegression()

# Define the predictor variable and target variable
X = df[['highway-mpg']]
Y = df['price']

# Then use lm.fit(X, Y) to fit the model (find the parameters b0 and b1)
lm.fit(X, Y)

# Then we obtain a prediction:
Yhat = lm.predict(X)

# The output is an array, it as the same number of samples as the input X

# The intersept and slope are attributes of the object lm, we can get them with:
lm.intercept_
lm.coef_

# So the equation is just substitute the values

# MULTIPLE LINEAR REGRESSION:
Y = b0 + b1*x1 + b2*x2 + b3*x3 + b4*x4 
# b0 is the intercept
# b1 is the coeficient of parameter of x1 (and so on)