import pika
import json
import uuid
import time

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

#otwarto połączenie z serwerem RabbitMQ
#nazwa kolejki to 'hello'
channel.queue_declare(queue='tasks')

def generate_json():
    data = {
        "uuid": str(uuid.uuid4()),
        "timestamp": int(time.time())
    }
    return json.dumps(data)

for i in range(100):
    channel.basic_publish(exchange='',
                        routing_key='tasks',
                        body=f'{generate_json()}')
print(" [x] Sent 'Hello World!'")

connection.close()