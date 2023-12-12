from flask import Flask

# Create a Flask app
app = Flask(__name__)

# Define a route for the homepage
@app.route('/')
def hello_world():
    return 'Hello, World!'

# Run the app if this file is executed
if __name__ == '__main__':
    app.run()

