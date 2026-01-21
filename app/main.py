from flask import Flask

def create_app():
    app = Flask(__name__)

    @app.route("/")
    def home():
        return "🚀 Python App Deployed with GitHub Actions CI/CD!"

    @app.route("/health")
    def health():
        return {"status": "ok"}

    return app
