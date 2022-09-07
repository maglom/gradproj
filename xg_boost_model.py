import pandas as pd
import numpy as np
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import StandardScaler, MinMaxScaler, OrdinalEncoder
from sklearn.model_selection import train_test_split
import xgboost
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.linear_model import LogisticRegression, LinearRegression
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_error

df_orig = pd.read_csv('TestTotal.csv', delimiter=';')

df = df_orig.copy()

# remove unwanted columns
df = df.drop(['Column1', 'Year'], axis=1)

# create a variable with the columns we wan to scale
columns_to_scale = df.iloc[:, 2:]

# importing scaler
scaler = MinMaxScaler()

# Scaling the columns
scaler.fit(columns_to_scale)
scaled_columns = scaler.transform(columns_to_scale)

# Import scaled columns back to the df
df.iloc[:,2:] = scaled_columns

# Encode the labels to numbers
ord = OrdinalEncoder()
ord.fit(df[['Wine']])
trans = ord.transform(df[['Wine']])
df['Wine'] = trans

# Classification
X = df
X = X.drop('Score', axis=1)
y = df['Score']

# # Convert to np array
# X = np.c_[df[X_columns]]
# y = np.c_[df[y_columns]]
# y = y.reshape(-1)

# Divide into test, train, split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Random forest prep
model = GradientBoostingRegressor(max_depth=2, n_estimators=200)
model.fit(X, y)

errors = [mean_squared_error(y_val, y_pred) for y_pred in model.staged_predict(X_val)]
best_n_estimator = np.argmin(errors)

# Train the model wiith XGBoost  :   eval_set=[(X_val, y_val)], early_stopping_rounds=2
model = xgboost.XGBRegressor()
model.fit(X_train, y_train)

y_test_pred = model.predict(X_test)

test_mse = mean_squared_error(y_test, y_test_pred)
test_mae = mean_absolute_error(y_test, y_test_pred)

print(f'test_mse: {test_mse}')
print(f'test_mae: {test_mae}')