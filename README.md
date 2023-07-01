# Customer Segmentation
Este proyecto tiene como objetivo realizar la segmentación de clientes utilizando un modelo de Random Forest Classifier. Se utiliza un conjunto de datos que contiene información demográfica y comportamental de los clientes de un centro comercial.

# Archivos
segmentation data.csv: Archivo CSV que contiene el conjunto de datos utilizado para el entrenamiento y prueba del modelo.

preprocessing.py: Archivo Python que realiza el preprocesamiento de los datos, incluyendo la transformación de las características numéricas.

model.py: Archivo Python que entrena el modelo de Random Forest Classifier y realiza predicciones.

app.py: Archivo Python que implementa una interfaz web utilizando Flask para enviar datos de entrada al modelo y mostrar los resultados de las predicciones.

templates/index.html: Archivo HTML que define el formulario de entrada para la interfaz web.

templates/result.html: Archivo HTML que muestra el resultado de las predicciones en la interfaz web.

# Instalación
Clona este repositorio en tu máquina local.

Asegúrate de tener Python 3.x instalado en tu sistema.

Instala las dependencias necesarias ejecutando el siguiente comando:

# Copy code
pip install -r requirements.txt
# Uso
Asegúrate de tener el archivo segmentation data.csv en la misma carpeta que los archivos preprocessing.py y model.py.

Ejecuta el archivo preprocessing.py para realizar el preprocesamiento de los datos.

Ejecuta el archivo model.py para entrenar el modelo y realizar predicciones.

Para ejecutar la interfaz web, ejecuta el archivo app.py y accede a http://localhost:5000 en tu navegador.

Ingresa los datos requeridos en el formulario y haz clic en "Predict" para obtener el resultado de la predicción.

# Contribución
Si deseas contribuir a este proyecto, puedes seguir los siguientes pasos:

Haz un fork de este repositorio.

Crea una rama para tu nueva funcionalidad (git checkout -b feature/nueva-funcionalidad).

Realiza los cambios y commits necesarios.

Haz un push de tu rama (git push origin feature/nueva-funcionalidad).

Crea una solicitud de pull en este repositorio.

# Autores
Roberto Jimenez Garcia - Desarrollo inicial

Si necesitas más información o detalles específicos, no dudes en proporcionarlos y estaré encantado de ayudarte a completar el contenido del archivo README.
