from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load trained model
model = pickle.load(open("model/model.pkl", "rb"))

# Model metrics
R2_SCORE = 0.88
MAE = 4.19


@app.route("/")
def home():
    return render_template(
        "index.html",
        r2=R2_SCORE,
        mae=MAE
    )


@app.route("/predict", methods=["POST"])
def predict():

    gender = int(request.form["gender"])
    lunch = int(request.form["lunch"])
    prep = int(request.form["prep"])
    reading = int(request.form["reading"])
    writing = int(request.form["writing"])

    features = np.array(
        [[gender, lunch, prep, reading, writing]]
    )

    prediction = model.predict(features)[0]

    return render_template(
        "index.html",
        prediction_text=f"Predicted Math Score: {prediction:.2f}",
        r2=R2_SCORE,
        mae=MAE
    )


if __name__ == "__main__":
    app.run(debug=True)