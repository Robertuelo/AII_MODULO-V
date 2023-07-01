from flask import Flask, render_template, request
import pandas as pd
import pickle

app = Flask(__name__, template_folder='templates')

# Cargar el modelo entrenado
with open('modelos/modelo_random_forest.pkl', 'rb') as file:
    modelo = pickle.load(file)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Obtener los datos de entrada del formulario
    sex = int(request.form['sex'])
    marital_status = int(request.form['marital_status'])
    age = int(request.form['age'])
    income = float(request.form['income'])
    occupation = int(request.form['occupation'])
    settlement_size = int(request.form['settlement_size'])

    # Crear un nuevo registro con los datos ingresados
    new_data = [[sex, marital_status, age, income, occupation, settlement_size]]

    # Realizar la predicción
    clase_predicha = modelo.predict(new_data)

    # Renderizar la plantilla de resultados
    return render_template('result.html', prediction=clase_predicha[0])

if __name__ == '__main__':
    app.run(debug=True)
