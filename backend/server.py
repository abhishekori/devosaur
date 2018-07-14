from flask import Flask, request
import uuid
from firebase import Firebase

app = Flask(__name__)

fb = Firebase()

@app.route('/health-check', methods = ['GET', 'POST'])
def healthCheck():
    return "Success"

@app.route('/getState')
def getState():
    state = uuid.uuid4()
    fb.addState(state)
    return str(state)

if __name__ == '__main__':
   app.run(debug=True,host = '0.0.0.0')
