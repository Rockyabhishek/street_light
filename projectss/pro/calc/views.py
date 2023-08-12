from django.shortcuts import render

# Create your views here.
import pyrebase

Config = {
  "apiKey": "AIzaSyCZX_R5kM-wYFgiBAXCEKkE4e7KIIUqK8o",
  "authDomain": "smart-street-light-9e646.firebaseapp.com",
  "databaseURL": "https://smart-street-light-9e646-default-rtdb.firebaseio.com",
  "projectId": "smart-street-light-9e646",
  "storageBucket": "smart-street-light-9e646.appspot.com",
  "messagingSenderId": "696986755874",
  "appId": "1:696986755874:web:929890eb009e9042057b7b",
  "measurementId": "G-BXN454MP3W"
}


firebase = pyrebase.initialize_app(Config)
auth = firebase.auth()
database = firebase.database()


def index(request):

    off_time = database.child("off_time").get().val()
    return render(request, 'index.html', {"off_time": off_time})