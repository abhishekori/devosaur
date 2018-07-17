from flask import Flask, request, redirect
from flask import jsonify
from flask_cors import CORS

import uuid

from firebase import Firebase
from githubAuth import GithubAuth

app = Flask(__name__)
CORS(app)

fb = Firebase()
github = GithubAuth()

@app.route('/health-check', methods = ['GET', 'POST'])
def healthCheck():
    return "Success"

@app.route('/login')
def getState():
    state = uuid.uuid4()
    fb.addState(state)
    return redirect("https://github.com/login/oauth/authorize?client_id=1f5665916a21c22763b5&state="+str(state))

@app.route('/auth_handler')
def authHandler():
    code =  request.args.get('code')
    state =  request.args.get('state')
    if fb.findState(state):
        accessToken = github.getAccessToken(code)
        return redirect("https://google.co.in?q="+accessToken,code=200)
    # TODO redirect to a error page
    # TODO write an error page
    return "Failure"

@app.route('/', methods = ['GET', 'POST'])
def rootApiCall():
    return "Success"

@app.route('/create-project',methods=['POST'])
def createProject():
    return jsonify(request.json)

if __name__ == '__main__':
   app.run(debug=True,host = '0.0.0.0')
