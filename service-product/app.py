from flask import Flask
app = Flask(__name__)

@app.route('/product')
def user():
    return {'product': 'Macbook Pro'}

app.run(host='0.0.0.0', port=5000)
