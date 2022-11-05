from flask import Flask, render_template, request, jsonify
import nishiCrypt as nc

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/encrypt")
def enc():
    return render_template("encrypt.html")

@app.route("/encdata", methods=['POST'])
def handleEnc():
    data = request.form.get('text')
    
    return jsonify(
        {
            'data': nc.encrypt(data)
        }
    )

@app.route("/decrypt")
def dec():
    return render_template("decrypt.html")

@app.route("/decdata", methods=['POST'])
def handleDec():
    data = request.form.get('text')
    
    return jsonify(
        {
            'data': nc.decrypt(data)
        }
    )

if __name__ == "__main__":
    app.run(debug=True)
