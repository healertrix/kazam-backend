from flask import Flask
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, Flask!'

if __name__ == '__main__':
    app.run(debug=True) 