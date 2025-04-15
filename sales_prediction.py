import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

# Sample dataset (replace this with your own CSV or database)
data = {
    'Month': [1, 2, 3, 4, 5, 6],
    'Sales': [200, 220, 250, 270, 300, 330]
}
df = pd.DataFrame(data)

# Features and labels
X = df[['Month']]         # Independent variable
y = df['Sales']           # Dependent variable

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
print(f"Mean Squared Error: {mse:.2f}")

# Predict future sales
future_months = pd.DataFrame({'Month': [7, 8, 9]})
future_sales = model.predict(future_months)
print("Predicted Sales for Future Months:")
print(future_sales)
