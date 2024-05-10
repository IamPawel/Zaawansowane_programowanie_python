import pika
import json
import time

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='tasks')

def callback(ch, method, properties, body):
    parsed = json.loads(body)
    print(f"Processing task: {parsed['uuid']}, timestamp: {parsed['timestamp']}")
    # Symulacja przetwarzania zadania
    time.sleep(3)
    print(f"Task completed: {parsed['uuid']}")
    
    # Wysłanie wiadomości zwrotnej o wykonaniu zadania
    channel.basic_publish(exchange='',
                          routing_key=properties.reply_to,
                          properties=pika.BasicProperties(correlation_id = \
                                                          properties.correlation_id),
                          body=json.dumps({"status": "completed", "uuid": parsed['uuid']}))
    ch.basic_ack(delivery_tag = method.delivery_tag)

channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue='tasks',
                      on_message_callback=callback)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()

connection.close()
