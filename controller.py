from flask import Flask, request, json
from flask import render_template
import uuid
import time
import json
import pika
import atexit



app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html')


connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='img_queue')

def produce(data):
    channel.basic_publish(exchange='',
                          routing_key='img_queue',
                          body=data)


@app.route('/imput_file', methods=['POST'])
def imput_file():
    img = request.files['file']
    id = str(uuid.uuid4())
    data = { 
        'uuid': id, 
        'timestamp': time.time(), 
        'file': img, 
        'type': 'file'}
    produce(data)
    return 'Sent data to queue', 200


@app.route('/url_from_disk', methods=['GET'])
def url_from_disk():
    path = request.args.get('url_from_disk')
    id = str(uuid.uuid4())
    data = { 
        'uuid': id, 
        'timestamp': time.time(), 
        'file': path, 
        'type': 'disk'}
    produce(data)
    return 'Sent data to queue', 200


@app.route('/url', methods=['GET'])
def url():
    url = request.args.get('url')
    id = str(uuid.uuid4())
    data = { 
        'uuid': id, 
        'timestamp': time.time(), 
        'file': url, 
        'type': 'link'}
    produce(data)
    return 'Sent data to queue', 200



def close_connection():
    connection.close()

# Zarejestruj funkcję close_connection do wywołania przy zamykaniu aplikacji
atexit.register(close_connection)

if __name__ == '__main__':
    app.run(debug=True)