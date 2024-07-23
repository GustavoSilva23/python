from flask import Flask
app = Flask(__name__)

@app.route('/')
def ola_mundo():
    return "eae suave"
@app.route("/sobre")
def pagina_sobre():
    return """ """
app.run(debug=True, port=8000)