
# Bird Classification App

Esta es una aplicación web para la clasificación de aves, que utiliza un modelo de TensorFlow para predecir la especie de un ave a partir de una imagen proporcionada por el usuario. La aplicación incluye un backend en Flask que maneja la predicción y un modelo entrenado guardado en formato `SavedModel`.

## Tabla de contenidos

- [Instalación](#instalación)
- [Uso](#uso)
- [Estructura del proyecto](#estructura-del-proyecto)
- [API Endpoints](#api-endpoints)
- [Modelo](#modelo)
- [Contribuciones](#contribuciones)
- [Licencia](#licencia)

## Instalación

Sigue los pasos a continuación para configurar y ejecutar la aplicación localmente.

### Requisitos

- Python 3.x
- TensorFlow 2.x
- Flask
- PIL (Python Imaging Library)
- Virtualenv (opcional, recomendado)

### Instrucciones

1. Clona el repositorio:
   ```bash
   git clone https://github.com/tu-usuario/bird-classification.git
   ```

2. Navega al directorio del proyecto:
   ```bash
   cd birdClassificationRN/backend
   ```

3. Crea un entorno virtual (opcional pero recomendado):
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate  # En Windows usa `.venv\Scripts\activate`
   ```

4. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

5. Ejecuta la aplicación Flask:
   ```bash
   python app.py
   ```

La aplicación debería estar ejecutándose en `http://127.0.0.1:5000`.

## Uso

La aplicación toma una imagen de un ave y devuelve la especie más probable basada en las predicciones del modelo.

### Ejemplo de uso

1. Envía una solicitud POST al endpoint `/` con una imagen de un ave.
2. Recibirás una respuesta JSON con la información de la especie predicha.

## Estructura del proyecto

```bash
birdClassificationRN/
│
├── backend/                 # Contiene el backend de la aplicación Flask
│   ├── app.py               # Código del backend y lógica de predicción
│   ├── decripcion.json      # Mapeo de clases del modelo a especies
│   └── [archivos de imágenes]  # Archivos de imagen para pruebas
│
├── modelo/                  # Contiene el modelo TensorFlow en formato SavedModel
│   └── modeloV1/            # Carpeta del modelo
│       ├── saved_model.pb   # Modelo guardado
│       ├── variables/       # Variables entrenadas del modelo
│       └── assets/          # Otros activos del modelo
│
├── frontend/                # (Posible implementación futura)
├── README.md                # Este archivo
├── requirements.txt         # Dependencias de Python
└── .gitignore               # Archivos que deben ser ignorados por Git
```

## API Endpoints

### POST `/`

Este endpoint recibe una imagen en formato JPEG o PNG y devuelve un JSON con la especie predicha.

- **Parámetros**: 
  - `file`: El archivo de imagen (JPEG o PNG).

- **Ejemplo de solicitud**:
  ```bash
  curl -X POST -F "file=@buho.JPG" http://127.0.0.1:5000/
  ```

- **Respuesta**:
  ```json
  {
    "especieInfo": {
      "especie": "Búho",
      "caracteristicas": "Ave rapaz nocturna.",
      "habitat": "Bosques y áreas rurales."
    }
  }
  ```

## Modelo

El modelo utilizado para la predicción es un modelo de TensorFlow guardado en el formato `SavedModel`. El modelo se encuentra en la carpeta `modelo/modeloV1/`. La arquitectura del modelo y los detalles de entrenamiento se encuentran en el archivo `implementacionModelo.ipynb`.

### Cómo actualizar el modelo

Para actualizar el modelo, reemplaza los archivos en `modelo/modeloV1/` con una nueva versión del modelo entrenado.

## Contribuciones

¡Las contribuciones son bienvenidas! Si deseas contribuir, por favor crea un fork del repositorio, realiza tus cambios y abre un pull request.

## Licencia

Este proyecto está bajo la licencia MIT. Consulta el archivo `LICENSE` para más detalles.
