import pyrebase
import firebase_admin
from firebase_admin import credentials

firebaseConfig = {
  apiKey: "AIzaSyC2jah77EY53J-7xPBtg3sru8fkExCQvJ4",
  authDomain: "api-ba-firebase.firebaseapp.com",
  databaseURL: "https://api-ba-firebase-default-rtdb.firebaseio.com/",
  projectId: "api-ba-firebase",
  storageBucket: "api-ba-firebase.appspot.com",
  messagingSenderId: "282711538023",
  appId: "1:282711538023:web:32dd2aaf7a106f8cf617c2"
}

cred = credentials.Certificate("./serviceAccountKey.json")
firebase_admin.initialize_app(cred)

link = "https://api-ba-firebase-default-rtdb.firebaseio.com/"

db = firebase.database()
users = db.child("users").get()

def stream_handler(message):
    print(message["event"]) # tipo de evento
    print(message["path"]) # caminho do nó
    print(message["data"]) # dados

my_stream = db.child("users").stream(stream_handler)