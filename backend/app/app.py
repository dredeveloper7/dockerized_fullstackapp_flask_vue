from flask import Flask, jsonify
import model
import logging
from flask_cors import CORS
logging.basicConfig(level=logging.INFO)

model_document = dict()

app = Flask(__name__)
CORS(app)  # This will enable CORS for all routes

# Simple model data (replace with your actual model)

@app.route('/')
def index():
    # import pdb; pdb.set_trace()
    # model.main(model_document)
    # return model.GMD
    return {'msg': 'Hello World'}

if __name__ == '__main__':
    app.run(debug=True, port=5000, host="0.0.0.0")
