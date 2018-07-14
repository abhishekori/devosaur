from flask import Flask, request, redirect
import uuid

from firebase import Firebase
from githubAuth import GithubAuth

app = Flask(__name__)

fb = Firebase()
github = GithubAuth()

@app.route('/health-check', methods = ['GET', 'POST'])
def healthCheck():
    return "Success"

@app.route('/getState')
def getState():
    state = uuid.uuid4()
    fb.addState(state)
    return str(state)

@app.route('/auth_handler')
def authHandler():
    code =  request.args.get('code')
    state =  request.args.get('state')
    if fb.findState(state):
        accessToken = github.getAccessToken(code)
        return redirect("https://google.co.in?q="+accessToken,code=200)
    return "Failure"
    #code=c689c12ca2f16bb49804&state=test

if __name__ == '__main__':
   app.run(debug=True,host = '0.0.0.0')
