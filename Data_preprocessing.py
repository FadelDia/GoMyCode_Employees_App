import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder

# Chargement des données
data = pd.read_csv('employee_performance.csv')

# Prétraitement des données
data = data.drop(columns=['employee_id', 'employee_name'])  # Suppression des colonnes non numériques

# Encodage des variables catégorielles
label_encoder = LabelEncoder()
data['gender'] = label_encoder.fit_transform(data['gender'])

# Séparation des features et de la cible
X = data[['hours_worked', 'training_hours', 'previous_performance', 'seniority', 'gender']]
y_performance = data['current_performance']
y_absences = data['absences']

# Normalisation des features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Séparation des données
X_train, X_test, y_train_performance, y_test_performance = train_test_split(X_scaled, y_performance, test_size=0.2, random_state=42)
X_train, X_test, y_train_absences, y_test_absences = train_test_split(X_scaled, y_absences, test_size=0.2, random_state=42)
