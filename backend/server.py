from flask import Flask, request
from flask import jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/health-check', methods = ['GET', 'POST'])
def healthCheck():
    return "Success"

@app.route('/', methods = ['GET', 'POST'])
def rootApiCall():
    return "Success"

@app.route('/create-project',methods=['POST'])
def createProject():
    return jsonify(request.json)


if __name__ == '__main__':
   app.run(host = '0.0.0.0')
