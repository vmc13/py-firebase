firebaseConfig = {
  "apiKey": "AIzaSyC2jah77EY53J-7xPBtg3sru8fkExCQvJ4",
  "authDomain": "api-ba-firebase.firebaseapp.com",
  "databaseURL": "https://api-ba-firebase-default-rtdb.firebaseio.com/",
  "projectId": "api-ba-firebase",
  "storageBucket": "api-ba-firebase.appspot.com",
  "messagingSenderId": "282711538023",
  "appId": "1:282711538023:web:32dd2aaf7a106f8cf617c2"
}



db = firebase.database()
from flask import Flask
from flask import request
import requests as r
import pyrebase

firebase = pyrebase.initialize_app(firebaseConfig)

app = Flask(__name__)


@app.route("/IOTSENSE/PINS", methods=["POST","GET"])
def handler():
    username = request.get_data()
    print(username.decode("utf-8"))
    username = username.decode("utf-8")
    result = [x.strip() for x in username.split(',')]
    print(result)

    db = firebase.database()
    users = db.child(device).child(child).get()
    print(users.val())

    def requestHandler(message):
        print(message["event"]) # put
        print(message["path"]) # /-K7yGTTEp7O549EzTYtI
        print(message["data"]) # {'title': 'Pyrebase', "body": "etc..."}

    my_stream = db.child("Data").stream(requestHandler)


    if r.status_code != 200:
     print( "Error:", r.status_code)
    return ""
