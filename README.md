# 🌐 AI-Enabled Secure IoT-Based Gas Monitoring System

---

## 📌 Project Overview

This project simulates an IoT-based gas monitoring system integrated with **Deep Learning, Cloud Computing, Software Engineering, Network Security, and Natural Language Processing (NLP)**.

The system generates environmental data (temperature and gas levels), sends it to a cloud platform, analyzes it using a trained machine learning model, stores results in a database, and allows users to interact using natural language queries.

---

## 🧱 System Architecture

```
Data Simulation → ThingSpeak Cloud and Thinkercad → Flask Backend → DL Model → MongoDB → NLP Interface
```

---

## ⚙️ Technologies Used

* Python
* Flask (Backend API)
* ThingSpeak (IoT Cloud Platform)
* MongoDB Atlas (Cloud Database)
* Scikit-learn (Deep Learning Model)
* Pandas, Requests
* Tinkercad (IoT Simulation)

---

## 📂 Project Structure

```
project/
│
├── backend/
│   ├── app.py
│   ├── requirements.txt
│
├── model/
│   ├── gas_model.pkl
│   ├── scaler.pkl
│
├── data_simulation/
│   ├── send_data.py
│
└── README.md
```

---

## 🚀 Setup Instructions

### 1. Install Dependencies

```bash
pip install -r backend/requirements.txt
```

---

### 2. Run Data Simulation

```bash
python data_simulation/send_data.py
```

* This script continuously sends temperature and gas data to ThingSpeak every 15 seconds.

---

### 3. Run Backend Server

```bash
cd backend
python app.py
```

* Server runs at:
  👉 http://127.0.0.1:5000

---

## 🔗 API Endpoints

---

### 🔹 1. Predict Risk

```
/predict/<API_KEY>
```

Example:

```
http://127.0.0.1:5000/predict/mysecurekey123
```

Response:

```json
{
  "temperature": 32,
  "gas": 600,
  "risk": "Danger"
}
```

---

### 🔹 2. Natural Language Query

```
/ask/<API_KEY>/<query>
```

Examples:

```
/ask/mysecurekey123/is environment safe
/ask/mysecurekey123/gas level
/ask/mysecurekey123/temperature
/ask/mysecurekey123/full status
```

---

### 🔹 3. View History (MongoDB)

```
/history/<API_KEY>
```

Example:

```
http://127.0.0.1:5000/history/mysecurekey123
```

Returns last stored records.

---

### 🔹 4. Unauthorized Access

```
/predict
/ask
```

Returns:

```json
{
  "error": "Unauthorized access"
}
```

---

## 🔄 Data Flow

1. Python script generates simulated sensor data
2. Data is sent to ThingSpeak cloud
3. Flask backend fetches latest data
4. Data is processed using trained ML model
5. Prediction is generated (Normal / Warning / Danger)
6. Results stored in MongoDB
7. User interacts via API or NLP queries

---

## 🧠 Deep Learning Model

* Model: Neural Network (MLPClassifier)
* Inputs: Temperature, Gas Level
* Outputs:

  * 0 → Normal
  * 1 → Warning
  * 2 → Danger
* Preprocessing: StandardScaler
* Model trained using simulated dataset

---

## 🔐 Security Implementation

* API key-based authentication
* Unauthorized access restricted
* Secure endpoints for all operations

---

## 📊 Cloud Usage

* ThingSpeak:

  * Real-time data storage
  * Visualization (graphs)
* MongoDB Atlas:

  * Persistent storage
  * Historical data tracking

---

## 💬 NLP Implementation

* Rule-based NLP system
* Processes user queries like:

  * “Is environment safe?”
  * “Gas level”
  * “Temperature”
* Returns intelligent responses

---

## 🧪 Software Engineering Implementation

* Modular architecture (separate folders)
* REST API design using Flask
* Separation of concerns (data, backend, ML, storage)
* Scalable and maintainable code structure
* Functional testing of APIs

---

## 📚 Subject-wise Implementation

---

### 🔹 Deep Learning (DL)

* Neural network model for risk prediction
* Data preprocessing using scaling
* Classification of environmental conditions
* Model trained and integrated into backend

---

### 🔹 Cloud Computing (CC)

* ThingSpeak used for IoT cloud data ingestion
* MongoDB Atlas used for cloud database storage
* Real-time data access via APIs
* Cloud-based visualization and monitoring

---

### 🔹 Software Engineering (SE)

* Modular system design
* RESTful API architecture
* Separation of components
* Maintainable and scalable structure

---

### 🔹 Network Security (NS)

* API key authentication
* Access control for endpoints
* Protection against unauthorized access
* Secure communication design

---

### 🔹 Natural Language Processing (NLP)

* Rule-based query processing
* User interaction via natural language
* Dynamic response generation
* Integration with backend and ML model

---

## 🎯 Conclusion

This project demonstrates a complete integration of IoT simulation, cloud computing, deep learning, and secure software systems with user-friendly interaction using NLP.

---
