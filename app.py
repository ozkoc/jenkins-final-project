from flask import Flask
import socket
import os

app = Flask(__name__)

@app.route("/")
def home():
    environment = os.getenv("APP_ENV", "unknown")
    hostname = socket.gethostname()
    return f"""
    <h1>Jenkins CI/CD Final Project</h1>
    <p>Environment: {environment}</p>
    <p>Pod: {hostname}</p>
    <p>Status: Running successfully 🚀</p>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
