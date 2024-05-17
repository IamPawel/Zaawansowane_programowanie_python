from flask import Flask, request, json
from flask import render_template
import uuid
import time
import json
import pika
import base64


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
    base64_content = base64.b64encode(img_content).decode("utf-8")
    id = str(uuid.uuid4())
    data = {
        "uuid": id,
        "timestamp": time.time(),
        "file": base64_content,
        "type": "file",
    }
    produce(str(data))
    return json.dumps(data)


@app.route("/url_from_disk", methods=["POST"])
def url_from_disk():
    path = request.args.get("url_from_disk")
    id = str(uuid.uuid4())
    data = {"uuid": id, "timestamp": time.time(), "file": path, "type": "disk"}
    produce(str(data))
    return json.dumps(json.dumps(data))


@app.route("/url", methods=["POST"])
def url():
    url = request.args.get("url")
    id = str(uuid.uuid4())
    data = {"uuid": id, "timestamp": time.time(), "file": url, "type": "link"}
    produce(str(data))
    return json.dumps(data)


def produce(message):
    channel.basic_publish(exchange="", routing_key="img_queue", body=message)


if __name__ == "__main__":
    app.run(debug=True)
