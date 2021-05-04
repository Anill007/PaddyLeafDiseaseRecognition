from flask import Flask, render_template, request

import os

import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

app = Flask(__name__)

current_directory = os.getcwd()
upload_destination = current_directory + "\\static\\uploaded\\"


@app.route('/main/')
def main():
    return render_template("main.html")


@app.route('/disease/')
def disease():
    return render_template("disease.html")


@app.route('/classifier/')
def home():
    return render_template("index.html")


@app.route('/result/', methods=['post'])
def result():

    if request.files["img"]:

        uploaded_image = request.files["img"]

        model = load_model("./static/models/paddytest.h5")
        img_width, img_height = 128, 128

        uploaded_image.save(os.path.join(
            upload_destination, uploaded_image.filename))

        img = image.load_img('./static/uploaded/{}'.format(uploaded_image.filename),
                             target_size=(img_width, img_height))

        img = image.img_to_array(img)
        img = np.expand_dims(img, axis=0)

        result = model.predict(img)

        prediction = np.round(result)

        CATEGORIES = ['Blast', 'Blight', 'Brownspot', 'Healthy']

        for i in range(4):
            if prediction[0][i] == 1:
                result = CATEGORIES[i]

    return render_template("result.html", output=result, imagename=uploaded_image.filename)


if __name__ == "__main__":
    app.run(debug=True)
