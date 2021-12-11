# cs6220FaceDetection

This repository contains the server for our cs6220 Face Detection Project. `server.py` is the flask server, `image_finder` takes a person's photo and looks up their name with [DeepFace](https://github.com/serengil/deepface), and `abalation.py` lets us test the accuracy of the model we use on our dataset. We use the Celeb-A dataset found [here](https://mmlab.ie.cuhk.edu.hk/projects/CelebA.html).

## Running the app

You can run the server by making sure you have all the python dependencies needed (including DeepFace), and running `FLASK_APP=server flask run`. Flask will say the url that you are supposed to make calls to.

You can download the dependencies by running `pip install -r requirements.txt`


## Requirements 

Python >= 3.7 is required
