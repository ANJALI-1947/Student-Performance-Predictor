import pandas as pd

# Load dataset
df = pd.read_csv("data/StudentsPerformance.csv")

# Check dataset
print(df.info())

print("\nMissing Values:")
print(df.isnull().sum())

# Encode categorical columns
from sklearn.preprocessing import LabelEncoder

le = LabelEncoder()

df["gender"] = le.fit_transform(df["gender"])
df["lunch"] = le.fit_transform(df["lunch"])
df["test preparation course"] = le.fit_transform(
    df["test preparation course"]
)

print("\nAfter Encoding:")
print(df.head())

# Features and Target
X = df[
    [
        "gender",
        "lunch",
        "test preparation course",
        "reading score",
        "writing score"
    ]
]

y = df["math score"]

# Split Dataset
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Train Model
from sklearn.linear_model import LinearRegression

model = LinearRegression()

model.fit(X_train, y_train)

# Make Predictions 
predictions = model.predict(X_test)

# Evaluate Model
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import r2_score

print("\nMAE:", mean_absolute_error(y_test, predictions))
print("R2 Score:", r2_score(y_test, predictions))

# Save Model
import pickle

pickle.dump(model, open("model/model.pkl", "wb"))

print("\nModel Saved Successfully")