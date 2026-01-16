from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load model, scaler, and feature list
with open("breast_cancer_model.pkl", "rb") as f:
    data = pickle.load(f)
    model = data["model"]
    scaler = data["scaler"]
    features = data["features"]

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    # Extract inputs in the same order as features
    input_values = []
    for feat in features:
        val = float(request.form[feat])
        input_values.append(val)

    X = np.array(input_values).reshape(1, -1)
    X_scaled = scaler.transform(X)
    pred = model.predict(X_scaled)[0]

    # Map 2/4 to human-readable labels
    label = "Benign (2)" if pred == 2 else "Malignant (4)"

    return render_template("index.html", prediction=label)

if __name__ == "__main__":
    app.run(debug=True)
