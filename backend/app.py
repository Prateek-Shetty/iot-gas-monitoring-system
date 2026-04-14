from flask import Flask, jsonify
import requests
import joblib
import pandas as pd
from pymongo import MongoClient
from datetime import datetime



app = Flask(__name__)

client = MongoClient()  #replace with your MongoDB connection string for showing the cloud
db = client["iot_project"]
collection = db["sensor_data"]

# Load model and scaler
model = joblib.load("../model/gas_model.pkl")
scaler = joblib.load("../model/scaler.pkl")

# ====== SECRETS ======
CHANNEL_ID = ""
READ_API_KEY = ""
API_SECRET_KEY = ""

# Labels
labels = ["Normal", "Warning", "Danger"]


@app.route("/")
def home():
    return "Backend Running!"


# ====== PREDICT ROUTE ======
@app.route("/predict")
def predict_no_key():
    return jsonify({"error": "Unauthorized access"}), 401
@app.route("/predict/<key>")
def predict(key):
    if key != API_SECRET_KEY:
        return jsonify({"error": "Unauthorized access"}), 401

    url = f"https://api.thingspeak.com/channels/{CHANNEL_ID}/feeds.json?api_key={READ_API_KEY}&results=1"

    response = requests.get(url)
    data = response.json()
    feed = data["feeds"][0]

    temperature = float(feed["field1"])
    gas = float(feed["field2"])

    input_df = pd.DataFrame([[temperature, gas]], columns=["temperature", "gas"])
    scaled_input = scaler.transform(input_df)

    prediction = model.predict(scaled_input)[0]

    collection.insert_one({
    "temperature": temperature,
    "gas": gas,
    "risk": labels[prediction],
    "timestamp": datetime.now()
    })


    return jsonify({
        "temperature": temperature,
        "gas": gas,
        "risk": labels[prediction]
    })


# ====== NLP ROUTE ======

@app.route("/ask")
def ask_no_key():
    return jsonify({"error": "Unauthorized access"}), 401
@app.route("/ask/<key>/<query>")
def ask(key, query):
    if key != API_SECRET_KEY:
        return jsonify({"error": "Unauthorized"}), 401

    query = query.lower()

    url = f"https://api.thingspeak.com/channels/{CHANNEL_ID}/feeds.json?api_key={READ_API_KEY}&results=1"
    response = requests.get(url)
    data = response.json()
    feed = data["feeds"][0]

    temperature = float(feed["field1"])
    gas = float(feed["field2"])

    input_df = pd.DataFrame([[temperature, gas]], columns=["temperature", "gas"])
    scaled_input = scaler.transform(input_df)

    prediction = model.predict(scaled_input)[0]
    risk = labels[prediction]

    if "safe" in query or "risk" in query:
        return jsonify({"response": f"Environment is {risk}"})

    elif "gas" in query:
        return jsonify({"response": f"Gas level is {gas}"})

    elif "temperature" in query:
        return jsonify({"response": f"Temperature is {temperature}°C"})

    elif "status" in query or "all" in query:
        return jsonify({
            "temperature": temperature,
            "gas": gas,
            "risk": risk
        })
    
    elif "history" in query:
         return jsonify({"response": "Use /history API to view past data"})

    else:
        return jsonify({"response": "Sorry, I didn't understand your question."})
    

@app.route("/history/<key>")
def history(key):
    if key != API_SECRET_KEY:
        return jsonify({"error": "Unauthorized"}), 401

    data = list(collection.find({}, {"_id": 0}).sort("timestamp", -1).limit(10))

    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)