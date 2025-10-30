import streamlit as st
import requests

st.set_page_config(page_title="🏠 House Price Prediction", page_icon="🏠", layout="centered")

st.title("🏠 House Price Prediction App")
st.write("Enter details below and get the estimated house price instantly!")

# Input fields
area = st.number_input("Area (in sq ft)", min_value=500, max_value=10000, value=3000)
bedrooms = st.number_input("Number of Bedrooms", min_value=1, max_value=10, value=3)
bathrooms = st.number_input("Number of Bathrooms", min_value=1, max_value=5, value=2)
stories = st.number_input("Number of Stories", min_value=1, max_value=3, value=2)
parking = st.number_input("Parking Spaces", min_value=0, max_value=5, value=1)

# Predict button
if st.button("🔍 Predict Price"):
    # Send data to FastAPI
    input_data = {
        "area": area,
        "bedrooms": bedrooms,
        "bathrooms": bathrooms,
        "stories": stories,
        "parking": parking
    }

    try:
        response = requests.post("http://127.0.0.1:8000/predict", json=input_data)
        if response.status_code == 200:
            result = response.json()
            st.success(f"🏡 **Predicted Price:** ₹{result['predicted_price']:,.2f}")
        else:
            st.error(f"API Error: {response.status_code}")
    except Exception as e:
        st.error(f"Connection Error: {e}")
