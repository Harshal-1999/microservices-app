from flask import Flask
app = Flask(__name__)

@app.route('/user')
def user():
    return {'user': 'Harshal'}

app.run(host='0.0.0.0', port=5000)
