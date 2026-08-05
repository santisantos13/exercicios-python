from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/ola")
def ola():
    return jsonify({"mensagem": "Olá, mundo!"})

if __name__ == "__main__":
    app.run(debug=True)