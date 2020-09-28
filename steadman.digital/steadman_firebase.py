import pyrebase

config = {
    "apiKey": "AIzaSyBX4w25Zq47tZgILdzWQtQF7rjwsjOaMtI",
    "authDomain": "chat-app-30309.firebaseapp.com",
    "databaseURL": "https://chat-app-30309.firebaseio.com",
    "projectId": "chat-app-30309",
    "storageBucket": "chat-app-30309.appspot.com",
    "messagingSenderId": "380798510663",
    "appId": "1:380798510663:web:5c04d27de2a9290bd7b362",
    "measurementId": "G-0DSLDZ7JP3"
}
firebase = pyrebase.initialize_app(config)

auth = firebase.auth()
#user = auth.create_user_with_email_and_password(email, password)
#user = auth.sign_in_with_email_and_password(email, password)