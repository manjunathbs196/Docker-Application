from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return 'This is a GET method'
    elif request.method == 'POST':
        return 'This is a POST method'
    else:
        return 'Unsupported method'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
