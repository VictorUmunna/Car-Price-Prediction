import streamlit as st
import pickle
import numpy as np
from sklearn.preprocessing import LabelEncoder
from lightgbm import LGBMRegressor

def load_model():
    with open('./models/regressor.pkl', 'rb') as file:
        data = pickle.load(file)
    return data

data = load_model()

model = data["model"]
norm = data['normalization']

le_manufacturer = LabelEncoder()
le_engine = LabelEncoder()
le_transmission = LabelEncoder()

def main():
    st.title("USED CAR PRICE PREDICTION APP")

    st.write("""### We need some information to predict the price""")

    manufacturers = (
        'Abarth', 'Alfa-Romero', 'Audi', 'BMW', 'Bentley', 'Chevrolet',
       'Chrysler', 'Citroen', 'DS', 'Dacia', 'Fiat', 'Ford', 'Honda',
       'Hyundai', 'Infiniti', 'Isuzu', 'Jaguar', 'Jeep', 'Kia',
       'Land-Rover', 'Lexus', 'MG', 'Maserati', 'Mazda', 'Mercedes-Benz',
       'Mini', 'Mitsubishi', 'Nissan', 'Peugeot', 'Porsche', 'Renault',
       'Seat', 'Skoda', 'Smart', 'Subaru', 'Suzuki', 'Toyota', 'Vauxhall',
       'Volkswagen', 'Volvo'
    )

    engines = (
        'Diesel', 
        'Electric',
        'Hybrid', 
        'Petrol', 
        'Plug_in_hybrid'
    )

    transmissions = (
        'Automatic',
        'Manual',
        'Semiautomatic'
    )

    manufacturer = st.selectbox("Manufacturer", manufacturers)
    age = st.slider("Age of Car", 1, 50, 1)
    mileage = st.text_input("Mileage","Type Here", max_chars = 6)
    engine = st.selectbox("Engine", engines)
    transmission = st.selectbox("Transmission", transmissions)

    ok = st.button("Predict Price")

    if ok:
        X = np.array([[manufacturer, age, mileage, engine, transmission]])
        X[:,0] = le_manufacturer.fit_transform(X[:,0])
        X[:,3] = le_engine.fit_transform(X[:,3])
        X[:,4] = le_transmission.fit_transform(X[:,4])
        scaled_X = norm.transform(X)

        price = model.predict(scaled_X)
        # convert the price from log_price to actual price
        actual_price = np.exp(price) + 1
        actual_price = round(actual_price[0])  # round to the neaarest Pounds

        st.subheader(f"The estimated cost of the car is {actual_price:,} pounds")


if __name__=='__main__':
    main()