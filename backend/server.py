from flask import Flask, request

app = Flask(__name__)


@app.route('/health-check', methods = ['GET', 'POST'])
def healthCheck():
    return "Success"

if __name__ == '__main__':
   app.run(host = '0.0.0.0')
