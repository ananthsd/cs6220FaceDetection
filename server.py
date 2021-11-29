# import os
from flask import Flask, flash, request, redirect, jsonify

from image_finder import find_image
from wikipedia import get_wikipedia_results
# from PIL import Image
# import io

app = Flask(__name__)

@app.route('/search', methods=['POST'])
def upload_file():
    print("headers",request.headers)
    print("form",request.form)
    print("image",request.files)

    file = request.files['image']
    # print("file", file)
    file.save("test.png")
    name = find_image("test.png")
    if name == None:
        output = {"error":True}
    else:
        output = {"id":0, "name": name, "wikipedia": get_wikipedia_results(name), "error": False}
    return jsonify(output)

@app.route('/', methods=['GET'])
def helloWorld():
    return "Hello World"

@app.route('/test', methods=['GET'])
def testParse():
    image_name = request.args.get('file')
    print(image_name)
    name = find_image(image_name)
    if name == None:
        output = {"error":True}
    else:
        output = {"name": name, "wikipedia": get_wikipedia_results(name), "error": False}
    return jsonify(output)