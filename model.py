# retrain_model.py or inside a Jupyter cell

import pandas as pd
import pickle
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Step 1: Load CSV
print("Loading dataset...")
try:
    df = pd.read_csv("Crop_recommendation.csv")
    print("✅ Dataset loaded successfully.")
except FileNotFoundError:
    print("❌ ERROR: 'Crop_recommendation.csv' not found in this directory.")
    exit()

# Step 2: Prepare Features and Target
X = df[["N", "P", "K", "temperature", "humidity", "ph", "rainfall"]]
y = df["label"]

# Step 3: Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 4: Train Model
print("Training RandomForestClassifier...")
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Step 5: Evaluate (optional)
accuracy = accuracy_score(y_test, model.predict(X_test))
print(f"✅ Model trained with accuracy: {accuracy:.2f}")

# Step 6: Save Model
pickle.dump(model, open("model.pkl", "wb"))
print("✅ Model saved to model.pkl")
