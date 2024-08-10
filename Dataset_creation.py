import pandas as pd
import numpy as np
from faker import Faker

# Nombre d'employés
n_employees = 350

# Génération des données
np.random.seed(42)  # Pour la reproductibilité
fake = Faker()

employee_ids = np.arange(1, n_employees + 1)
employee_names = [fake.name() for _ in range(n_employees)]
hours_worked = np.random.randint(30, 60, size=n_employees)  # Heures travaillées entre 30 et 60 heures par semaine
training_hours = np.random.randint(0, 20, size=n_employees)  # Heures de formation entre 0 et 20 heures
previous_performance = np.random.randint(0, 10, size=n_employees)  # Performance précédente entre 0 et 10
current_performance = previous_performance + np.random.normal(0, 1, size=n_employees)  # Performance actuelle avec bruit
absences = np.random.poisson(lam=2, size=n_employees)  # Absences en utilisant une distribution de Poisson
seniority = np.random.randint(1, 21, size=n_employees)  # Ancienneté entre 1 et 20 ans
genders = np.random.choice(['Male', 'Female'], size=n_employees)  # Genre aléatoire

# Création du DataFrame
data = pd.DataFrame({
    'employee_id': employee_ids,
    'employee_name': employee_names,
    'hours_worked': hours_worked,
    'training_hours': training_hours,
    'previous_performance': previous_performance,
    'current_performance': current_performance,
    'absences': absences,
    'seniority': seniority,
    'gender': genders
})

# Sauvegarde dans un fichier Excel
data.to_excel('employee_performance.xls', index=False, engine='xlwt')

print("Dataset créé et sauvegardé sous 'employee_performance.xls'")
