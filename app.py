# Import dependencies
from flask import Flask

# Create Flask app instance
app = Flask(__name__)

# Create Flask route
@app.route('/')
def hello_world():
    return 'Hello world'