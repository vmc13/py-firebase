from flask import Flask
from pyrebase import pyrebase

firebaseConfig = {
  "apiKey": "AIzaSyC2jah77EY53J-7xPBtg3sru8fkExCQvJ4",
  "authDomain": "api-ba-firebase.firebaseapp.com",
  "databaseURL": "https://api-ba-firebase-default-rtdb.firebaseio.com/",
  "projectId": "api-ba-firebase",
  "storageBucket": "api-ba-firebase.appspot.com",
  "messagingSenderId": "282711538023",
  "appId": "1:282711538023:web:32dd2aaf7a106f8cf617c2"
}

firebase = pyrebase.initialize_app(firebaseConfig)

# auth = firebase.auth()
db = firebase.database()

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, Flask!"

if __name__ == "__main__":
    app.run()