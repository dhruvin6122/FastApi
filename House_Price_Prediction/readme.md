# 🏠 House Price Prediction — Full Stack Machine Learning App

A complete **end-to-end Machine Learning project** built with **FastAPI**, **Streamlit**, and **Scikit-Learn**.  
The app predicts **house prices** based on features such as area, number of bedrooms, bathrooms, stories, and parking.

This project demonstrates the full ML workflow — **data creation → model training → REST API → frontend UI**.

---

## 🚀 Tech Stack

| Layer | Technology |
|--------|-------------|
| **Machine Learning** | Scikit-Learn, Pandas, NumPy |
| **Backend API** | FastAPI |
| **Frontend UI** | Streamlit |
| **Language** | Python |
| **Model Serialization** | Joblib |

---

## 🧠 Project Overview

This project simulates a real-world **house price prediction system** with focus on clean architecture and full integration between ML, backend, and frontend.

### 🔹 Key Features
- Trains a **Linear Regression** model on synthetic housing data  
- Exposes prediction API using **FastAPI**  
- Interactive **Streamlit UI** for live prediction  
- Modular folder structure, easy to extend or deploy  

---

## 🏗️ Folder Structure




House_Price_Prediction/
│
├── data/
│ ├── generate_data.py # Script to generate synthetic dataset
│ └── house_data.csv # Generated dataset
│
├── backend/
│ ├── main.py # FastAPI backend server
│ └── model/
│ ├── train_model.py # Model training script
│ └── house_price_model.pkl # Saved ML model
│
├── frontend/
│ └── app.py # Streamlit app (frontend)
│
├── requirements.txt
└── README.md
