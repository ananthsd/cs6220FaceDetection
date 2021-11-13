import os
from flask import Flask, flash, request, redirect, jsonify
from PIL import Image
import io

app = Flask(__name__)

@app.route('/search', methods=['POST'])
def upload_file():
    print("headers",request.headers)
    print("form",request.form)
    print("image",request.files)

    file = request.files['image']
    # print("file", file)
    file.save("test.jpeg")
    output = {"id":0, "name": "Patrick Star", "links": ["url1","url2"]}
    return jsonify(output)

@app.route('/', methods=['GET'])
def helloWorld():
    return "Hello World"