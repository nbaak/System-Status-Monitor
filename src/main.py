from flask import Flask, render_template
from blueprints.status.status import status
import os


app = Flask(__name__)
app.register_blueprint(status)
app.config.update(
    PROJECT_ROOT = os.path.dirname(__file__)+'/'
)

@app.route("/")
def main():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=False, host = '0.0.0.0')