from flask import Flask

app = Flask(__name__)


@app.route("/api")
def api():
    return {
        "members": ["Gabriel", "Danny", "Oliver"]
    }


if __name__ == "__main__":
    app.run(debug=True)
