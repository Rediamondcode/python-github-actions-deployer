from flask import Flask, jsonify
import socket
import datetime

def create_app():
    app = Flask(__name__)

    APP_VERSION = "1.0.1"  # change this to test CI/CD
    DEPLOYED_AT = datetime.datetime.utcnow().isoformat() + "Z"
    HOSTNAME = socket.gethostname()

    @app.route("/")
    def home():
        return f"""
        🚀 Python App Deployed with GitHub Actions CI/CD!<br><br>
        <b>Version:</b> {APP_VERSION}<br>
        <b>Deployed at (UTC):</b> {DEPLOYED_AT}<br>
        <b>Server:</b> {HOSTNAME}
        """

    @app.route("/health")
    def health():
        return jsonify(
            status="ok",
            version=APP_VERSION,
            server=HOSTNAME
        )

    return app
