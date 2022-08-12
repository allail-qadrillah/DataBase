import pyrebase

firebase_config = {"YOUR FIREBASE CONFIG"} # get firebaseconfig == settungs -> project settings -- scroldown -- SDK setup and configuration

# Initialize app
firebase = pyrebase.initialize_app(firebase_config)

# Create variabel to store Build of Firebase Authentication 
auth = firebase.auth()

# AUTHENTICATION 
# Manage authentication login
def sign_in(email, password):
    try:
        auth.sign_in_with_email_and_password(str(email), str(password))
        print('login successfully')
    except:
        print('Email and password are incorrect!')
 
# Manage authentication sign up
def sign_up(email, password):
    try:
        auth.create_user_with_email_and_password(str(email), str(password))
        print('login successfully')
    except:
        print('Email already exist!')

