import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import config


# cred = credentials.Certificate("devosaur-x-firebase-adminsdk-qqwmn-3ee79b183e.json")
# firebase_admin.initialize_app(cred, {
#         'databaseURL': 'https://devosaur-x.firebaseio.com'
# })


class Firebase:

    def __init__(self):
        cred = credentials.Certificate('devosaur-x-firebase-adminsdk-qqwmn-3ee79b183e.json')
        firebase_admin.initialize_app(cred, {
                'databaseURL': config.config['databaseURL']
        })


    def addState(self,state):
        common_ref = db.reference('/common')
        states_ref = common_ref.child('states')
        states_ref.push(str(state))
