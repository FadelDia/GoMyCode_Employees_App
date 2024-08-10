import streamlit as st
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import StandardScaler, LabelEncoder

# Charger les modèles pré-entraînés
def load_models_and_scaler():
    global model_performance, model_absences, scaler, label_encoder

    # Charger les données pour scaler (si nécessaire)
    data = pd.read_excel('employee_performance.xls', engine='xlrd')
    X = data[['hours_worked', 'training_hours', 'previous_performance', 'seniority', 'gender']]
    scaler = StandardScaler()
    scaler.fit(X)
    label_encoder = LabelEncoder()
    label_encoder.fit(data['gender'])

    # Entraîner les modèles ici pour l'exemple
    y_performance = data['current_performance']
    y_absences = data['absences']
    X_scaled = scaler.transform(X)

    model_performance = LinearRegression()
    model_performance.fit(X_scaled, y_performance)

    model_absences = RandomForestRegressor(n_estimators=100, random_state=42)
    model_absences.fit(X_scaled, y_absences)

def predict_performance(hours_worked, training_hours, previous_performance, seniority, gender):
    X = np.array([[hours_worked, training_hours, previous_performance, seniority, gender]])
    X_scaled = scaler.transform(X)
    return model_performance.predict(X_scaled)[0]

def predict_absences(hours_worked, training_hours, previous_performance, seniority, gender):
    X = np.array([[hours_worked, training_hours, previous_performance, seniority, gender]])
    X_scaled = scaler.transform(X)
    return model_absences.predict(X_scaled)[0]

def main():
    st.title("Prédiction des Performances et de l'Assiduité des Employés")

    st.sidebar.header("Entrer les Données de l'Employé")

    hours_worked = st.sidebar.number_input("Heures travaillées par semaine", min_value=0, max_value=168, value=40)
    training_hours = st.sidebar.number_input("Heures de formation", min_value=0, value=5)
    previous_performance = st.sidebar.number_input("Performance précédente", min_value=0, max_value=10, value=7)
    seniority = st.sidebar.number_input("Ancienneté (années)", min_value=1, max_value=20, value=5)
    gender = st.sidebar.selectbox("Genre", ["Male", "Female"])
    gender_encoded = label_encoder.transform([gender])[0]

    if st.sidebar.button("Prédire"):
        performance = predict_performance(hours_worked, training_hours, previous_performance, seniority, gender_encoded)
        absences = predict_absences(hours_worked, training_hours, previous_performance, seniority, gender_encoded)

        st.write(f"**Performance Prédite**: {performance:.2f}")
        st.write(f"**Assiduité Prédite**: {absences:.2f}")

if __name__ == "__main__":
    load_models_and_scaler()  # Charger les modèles et scaler
    main()
