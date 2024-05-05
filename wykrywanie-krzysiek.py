import numpy as np
import cv2
import urllib.request
from flask import Flask, request, jsonify, Response, render_template_string

app = Flask(__name__)


def count_people(image):

    blurred_image = cv2.GaussianBlur(image, (5, 5), 0)


    gray_image = cv2.cvtColor(blurred_image, cv2.COLOR_BGR2GRAY)


    equalized_image = cv2.equalizeHist(gray_image)


    hog = cv2.HOGDescriptor()
    hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())


    boxes, _ = hog.detectMultiScale(equalized_image, winStride=(8, 8))


    for (x, y, w, h) in boxes:
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

    return len(boxes), image


def read_image_from_url(url):
    
    resp = urllib.request.urlopen(url)
    image = np.asarray(bytearray(resp.read()), dtype="uint8")
    image = cv2.imdecode(image, cv2.IMREAD_COLOR)
    return image


@app.route('/')
def index():
    return render_template_string('''
        <form action="/count_people_upload" method="post" enctype="multipart/form-data">
            <input type="file" name="file">
            <input type="submit" value="Upload Image">
        </form>

        <form action="/count_people_url" method="get">
            <input type="text" name="image_url" placeholder="Enter Image URL">
            <input type="submit" value="Submit">
        </form>

        <form action="/count_people" method="get">
            <input type="text" name="image_path" placeholder="Enter Image Path">
            <input type="submit" value="Submit">
        </form>
    ''')


@app.route('/count_people', methods=['GET'])
def count_people_from_disk():
    image_path = request.args.get('image_path')
    if not image_path:
        return jsonify({"error": "Please provide the path to the image"}), 400

    try:
        image = cv2.imread(image_path)
        count, image_with_rects = count_people(image)
        _, img_encoded = cv2.imencode('.png', image_with_rects)
        response = img_encoded.tobytes()
        return Response(response=response, content_type='image/png'), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/count_people_url', methods=['GET'])
def count_people_from_url():
    image_url = request.args.get('image_url')
    if not image_url:
        return jsonify({"error": "Please provide the URL to the image"}), 400

    try:
        image = read_image_from_url(image_url)
        count, image_with_rects = count_people(image)
        _, img_encoded = cv2.imencode('.png', image_with_rects)
        response = img_encoded.tobytes()
        return Response(response=response, content_type='image/png'), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/count_people_upload', methods=['POST'])
def count_people_from_upload():
    try:

        if 'file' not in request.files:
            return jsonify({"error": "No file part"}), 400
        file = request.files['file']
        if file.filename == '':
            return jsonify({"error": "No selected file"}), 400


        nparr = np.frombuffer(file.read(), np.uint8)
        image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        count, image_with_rects = count_people(image)
        _, img_encoded = cv2.imencode('.png', image_with_rects)
        response = img_encoded.tobytes()
        return Response(response=response, content_type='image/png'), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)
