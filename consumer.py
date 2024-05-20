import pika
import json
from detection import prepare_response

connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))

channel = connection.channel()
channel.queue_declare(queue="img_queue")
channel.basic_qos(prefetch_count=1)


def callback(ch, method, properties, body):
    data = json.loads(body)
    try:
        prepare_response(data)
        print(f"Detection people on file {data['uuid']} completed")
    except Exception as e:
        print(f"Detection people on file {data['uuid']} failed - Error: {e}")
    ch.basic_ack(delivery_tag=method.delivery_tag)


channel.basic_consume(queue="img_queue", auto_ack=False, on_message_callback=callback)

print("Waiting for messages. To exit press CTRL+C")
channel.start_consuming()

connection.close()
