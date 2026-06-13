# Reconocimiento Facial con Webcam

## Problema que Resuelve

Este proyecto resuelve el problema de identificar y registrar rostros utilizando una webcam. La aplicación permite capturar imágenes en tiempo real, detectar rostros y extraer características faciales para poder identificar a las personas.

## Tecnologías Usadas y Por Qué

### 1. OpenCV
- **Descripción**: Biblioteca de código abierto que ofrece herramientas para el procesamiento de imágenes y video.
- **Razón**: Utilizada para capturar video en tiempo real desde la webcam, detectar rostros y dibujar formas sobre los marcos.

### 2. Dlib
- **Descripción**: Biblioteca de código abierto que incluye un algoritmo de detección de rostros muy preciso.
- **Razón**: Proporciona modelos pre-entrenados para la extracción de características faciales (vectores) y detectar rostros en imágenes.

### 3. NumPy
- **Descripción**: Biblioteca fundamental para el cálculo numérico en Python, especialmente útil cuando trabajas con vectores de características faciales.
- **Razón**: Necesario para manipulación numérica eficiente y manejo de datos estructurados.

### 4. Flask o Django (opcional)
- **Descripción**: Frameworks web de Python que facilitan el desarrollo de aplicaciones web.
- **Razón**: Si se desea crear un backend web, estos frameworks pueden ser utilizados para manejar solicitudes del usuario y interactuar con la base de datos.

### 5. SQLite o MongoDB (opcional)
- **Descripción**: Bases de datos relacionales y no relacionales respectivamente.
- **Razón**: Para almacenar los datos del rostro (vectores) en una base de datos, permitiendo así identificar a las personas basándose en sus características faciales.

Este proyecto utiliza estas tecnologías para proporcionar un sistema robusto y eficiente de reconocimiento facial que puede ser utilizado en diversos contextos, desde seguridad hasta personalización de experiencias digitales.


## 6.Instrucciones de uso

- Clonar el proyecto y entrar a la carpeta
```
git clone https://github.com/NicolasBruna24/DeterctorRostro.git
cd DeterctorRostro
```
- Crear y activar su propio entorno virtual
```
python3 -m venv .venv
source .venv/bin/activate
```
- Instalar todo en un solo segundo

```
pip install -r requirements.txt
```
- Descargar el predictor de rostros
```
wget https://github.com/italojs/facial-landmarks-recognition/raw/master/shape_predictor_68_face_landmarks.dat
```
- ¡Ejecutar!
```
python main.py
```