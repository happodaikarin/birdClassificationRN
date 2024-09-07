from flask import Flask, request, jsonify
from flask_cors import CORS
import tensorflow as tf
import numpy as np
from PIL import Image
import io
import json

app = Flask(__name__)
CORS(app)

# Cargar el modelo de TensorFlow usando tf.saved_model.load()
modelo = tf.saved_model.load('modelo/modeloV1')
print("Model successfully loaded using tf.saved_model.load().")

# Use la firma 'serving_default' para ejecutar inferencias
infer = modelo.signatures['serving_default']

# Cargar mapeo de índices de clase a etiquetas de aves desde un archivo JSON
with open('decripcion.json', 'r') as file:
    indice_a_etiqueta = json.load(file)

# Cargar información adicional sobre las especies de aves desde un archivo JSON
with open('decripcion.json', 'r') as file:
    informacion_especies = json.load(file)

def preparar_imagen(imagen, tamaño_objetivo):
    if imagen.mode != "RGB":
        imagen = imagen.convert("RGB")
    imagen = imagen.resize(tamaño_objetivo)
    imagen = tf.keras.preprocessing.image.img_to_array(imagen)
    imagen = np.expand_dims(imagen, axis=0)

    return imagen

@app.route('/', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({'error': 'No se encontró el archivo'}), 400

    archivo = request.files['file']
    if archivo.filename == '':
        return jsonify({'error': 'No se seleccionó ningún archivo'}), 400

    imagen = Image.open(io.BytesIO(archivo.read()))
    imagen_preparada = preparar_imagen(imagen, (224, 224))  # Ajustar según el tamaño de entrada del modelo

    # Realizar la predicción usando la firma 'serving_default'
    predicciones = infer(tf.convert_to_tensor(imagen_preparada))['dense_14']

    # Aplicar softmax para obtener probabilidades
    probabilidades = tf.nn.softmax(predicciones, axis=1).numpy()

    # Imprimir las probabilidades para depuración
    print("Probabilidades: ", probabilidades)

    # Obtener la clase con mayor probabilidad
    clase_predicha = np.argmax(probabilidades, axis=1)[0]

    # Imprimir la clase predicha para depuración
    print("Clase predicha: ", clase_predicha)

    # Obtener información de la especie basada en la clase predicha
    especie_info = informacion_especies.get(str(clase_predicha), {
        'especie': 'Desconocida',
        'caracteristicas': 'No hay información disponible',
        'habitat': 'No hay información disponible'
    })
    
    response_data = {
        'especieInfo': especie_info
    }

    return jsonify(response_data)

if __name__ == '__main__':
    app.run(debug=True)
