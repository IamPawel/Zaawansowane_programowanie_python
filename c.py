import pika
import json
import time

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

#otwarto połączenie z serwerem RabbitMQ
#nazwa kolejki to 'hello'
channel.queue_declare(queue='tasks')
channel.basic_qos(prefetch_count=1)


def callback(ch, method, properties, body):
    parsed = json.loads(body)
    print(f"task: {parsed['uuid']}, timestamp: {parsed['timestamp']}")
    ch.basic_ack(delivery_tag = method.delivery_tag)

channel.basic_consume(queue='tasks',
                      auto_ack=False,
                      on_message_callback=callback)



print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()

connection.close()

#on może pobierać po kilka wiadomości na raz, zależy jak chcemy