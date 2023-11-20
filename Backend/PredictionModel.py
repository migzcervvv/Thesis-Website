import pandas as pd
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor, StackingRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split, KFold
from sklearn.metrics import mean_squared_error
from sklearn.linear_model import LinearRegression
import pickle

# Define your expanded dataset
data = pd.DataFrame({
    'Temperature': [24.5, 30, 22, 25, 28, 23, 26, 27, 21, 29, 20, 31],
    'Humidity': [40, 50, 35, 42, 48, 38, 45, 47, 33, 52, 34, 53],
    'PM2.5': [12, 20, 15, 13, 18, 16, 14, 19, 15, 17, 14, 21],
    'CO2': [400, 450, 380, 410, 430, 390, 420, 440, 370, 435, 365, 455],
    'SmogLevel': [20, 80, 50, 25, 70, 55, 30, 75, 45, 65, 40, 85]
})

# Creating new feature: Humidity-Temperature Index
data['HumidityTempIndex'] = data['Temperature'] * data['Humidity']

# Define features and target variable
X = data[['Temperature', 'Humidity', 'PM2.5', 'CO2', 'HumidityTempIndex']]
y = data['SmogLevel']

# Normalize the features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2)

# Define base learners
estimators = [
    ('rf', RandomForestRegressor(n_estimators=100)),
    ('gb', GradientBoostingRegressor(n_estimators=100))
]

# Create and train the Stacking model
stack_model = StackingRegressor(
    estimators=estimators,
    final_estimator=LinearRegression()
)
stack_model.fit(X_train, y_train)

# Make predictions and evaluate
predictions = stack_model.predict(X_test)
mse = mean_squared_error(y_test, predictions)
print(f'Mean Squared Error: {mse}')

# Feature Importance (from RandomForestRegressor)
rf_model = stack_model.named_estimators_['rf']
importances = rf_model.feature_importances_
print(f'Feature Importances from RandomForest: {importances}')

with open('Backend/model1.pkl', 'wb') as file:
    pickle.dump(stack_model, file)