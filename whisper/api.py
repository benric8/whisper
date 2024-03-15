
from whisper import load_model, predict

# Cargar el modelo Whisper
model = load_model("medium")

# Función para procesar una solicitud
def process_request(audio_file):
    # Leer el archivo de audio
    audio = audio_file.read()

    # Predecir la transcripción
    prediction = predict(model, audio)

    # Devolver la transcripción
    return prediction["text"]

# Importar Flask para crear la API
from flask import Flask, request, jsonify

# Crear la aplicación Flask
app = Flask(__name__)

# Ruta para la API
@app.route("/transcribe", methods=["POST"])
def transcribe():
    # Obtener el archivo de audio de la solicitud
    audio_file = request.files["audio"]

    # Procesar la solicitud y obtener la transcripción
    transcription = process_request(audio_file)

    # Devolver la transcripción como JSON
    return jsonify({"transcription": transcription})

# Iniciar la aplicación
if __name__ == "__main__":
    app.run(debug=True)