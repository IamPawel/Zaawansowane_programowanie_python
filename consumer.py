import pika
import json
import time

connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))

channel = connection.channel()
channel.queue_declare(queue="tasks")
channel.basic_qos(prefetch_count=1)


def callback(ch, method, properties, body):
    # body to jest to co przyszło z kolejki czyli u mnie json
    print(f"Message received: {body}")
    time.sleep(1)
    ch.basic_ack(delivery_tag=method.delivery_tag)
