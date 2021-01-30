import pika
import json

class Consumer():
    def consume(self):
        connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
        channel = connection.channel()

        channel.queue_declare(queue='test queue')

        print("[*] Waiting for messages. To exit press CTRL+C")

        def callback(ch, method, properties, body):
            print("[x] Received %r" % (body,))

        channel.basic_consume(on_message_callback=callback,
                            queue='test queue',
                            auto_ack=False)

        channel.start_consuming()
