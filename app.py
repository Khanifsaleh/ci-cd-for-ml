from flask import Flask
import joblib

# Create a Flask app
app = Flask(__name__)

# Define a route for the homepage
@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/get_model_name', methods=['GET'])
def get_model_name():
    return 'get_model_name'

# Run the app if this file is executed
if __name__ == '__main__':
    app.run()