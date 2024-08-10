from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error

# Entraînement du modèle de régression linéaire pour la performance
model_performance = LinearRegression()
model_performance.fit(X_train, y_train_performance)

# Entraînement du modèle de forêt aléatoire pour les absences
model_absences = RandomForestRegressor(n_estimators=100, random_state=42)
model_absences.fit(X_train, y_train_absences)

# Évaluation des modèles
y_pred_performance = model_performance.predict(X_test)
performance_rmse = mean_squared_error(y_test_performance, y_pred_performance, squared=False)
print(f"RMSE pour la performance : {performance_rmse}")

y_pred_absences = model_absences.predict(X_test)
absences_rmse = mean_squared_error(y_test_absences, y_pred_absences, squared=False)
print(f"RMSE pour les absences : {absences_rmse}")
