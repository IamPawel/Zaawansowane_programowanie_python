from flask import Flask, request, jsonify
from flask import render_template
import uuid
import time
import json
import pika
import base64
import cv2 as cv
import numpy as np

app = Flask(__name__)


@app.route("/")
def hello():
    return render_template("index.html")


connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
channel = connection.channel()
channel.queue_declare(queue="img_queue")


@app.route("/imput_file", methods=["POST"])
def imput_file():
    img = request.files["file"]
    img_content = img.read()
    np_arr = np.frombuffer(img_content, np.uint8)
    img_np = cv.imdecode(np_arr, cv.IMREAD_COLOR)
    _, img_encoded = cv.imencode(".jpg", img_np)
    img_base64 = base64.b64encode(img_encoded).decode("utf-8")
    data = generate_json(img_base64, "file")
    produce(f"{data}")
    return jsonify(data)


@app.route("/url_from_disk", methods=["POST"])
def url_from_disk():
    path = request.form.get("url_from_disk")
    data = generate_json(path, "path")
    produce(f"{data}")
    return jsonify(data)


@app.route("/url", methods=["POST"])
def url():
    url = request.form.get("url")
    data = generate_json(url, "link")
    produce(f"{data}")
    return jsonify(data)


def generate_json(file, type):
    data = {
        "uuid": str(uuid.uuid4()),
        "timestamp": time.time(),
        "file": file,
        "type": type,
    }
    return data


def produce(message):
    channel.basic_publish(exchange="", routing_key="img_queue", body=message)


if __name__ == "__main__":
    app.run(debug=True)
