from flask import Flask, send_from_directory
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

DIRECTORY = "C:/Users/hp/Downloads/SIGMA WEB DEVELOPMENT COURSE/Spotify clone/Songs"

@app.route('/<path:filename>')
def serve_song(filename):
    return send_from_directory(DIRECTORY, filename)

if __name__ == '_main_':
    app.run(host='0.0.0.0', port=8000)