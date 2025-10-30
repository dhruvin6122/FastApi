import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error
import joblib
import os

# make sure model folder exists
os.makedirs("backend/model", exist_ok=True)

# load dataset
df = pd.read_csv("house_data.csv")

# split features and target
X = df[["area", "bedrooms", "bathrooms", "stories", "parking"]]
y = df["price"]

# split into train/test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# train model
model = LinearRegression()
model.fit(X_train, y_train)

# evaluate model
y_pred = model.predict(X_test)
r2 = r2_score(y_test, y_pred)
import math
rmse = math.sqrt(mean_squared_error(y_test, y_pred))


print("✅ Model trained successfully")
print(f"R² Score: {r2:.4f}")
print(f"RMSE: {rmse:.2f}")

# save model
joblib.dump(model, "backend/model/house_price_model.pkl")
print("💾 Model saved as backend/model/house_price_model.pkl")
