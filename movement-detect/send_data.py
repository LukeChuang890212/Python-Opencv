#%%
import pika
import json
import time

from receive_data import Consumer

#%%
class Publisher():
     def publish(self,cnts):
        connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
        channel = connection.channel()

        channel.queue_declare(queue='test queue')

        
        
        for i in range(len(cnts)):
            cnts[i] = cnts[i].astype("int")
            cnts[i] = cnts[i].tolist()

        msg = dict(cnts=cnts)

        channel.basic_publish(exchange='',
                            routing_key='test queue',
                            body=json.dumps(msg))

        connection.close()
if __name__ == "__main__":
    publisher = Publisher()
    consumer = Consumer()

    msg = input("publish:")
    while msg != 0:
        msg = input("publish:")
        publisher.publish(msg)

        # time.sleep(5)
        # consumer.consume()
    print("end")
