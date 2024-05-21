from imports import *
from detection import prepare_response, read_json


connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))

channel = connection.channel()
channel.queue_declare(queue="img_queue")
channel.basic_qos(prefetch_count=1)


def callback(ch, method, properties, body):
    data = body.decode("utf-8")
    data = data.replace("'", '"')
    data = json.loads(data)
    try:
        count = prepare_response(data)
        print(
            f"Detection people on file {data['uuid']} completed. Number of people: {count}"
        )
    except Exception as e:
        print(f"Detection people on file {data['uuid']} failed - Error: {e}")
    ch.basic_ack(delivery_tag=method.delivery_tag)


channel.basic_consume(queue="img_queue", auto_ack=False, on_message_callback=callback)

print("Waiting for messages. To exit press CTRL+C")
channel.start_consuming()

connection.close()
