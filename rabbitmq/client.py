import time
import pika

def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)
    time.sleep(1)
    ch.basic_ack(delivery_tag = method.delivery_tag)  #发送ack消息

queue_name="test"
exchange_name="amq.fanout"

parameters = pika.URLParameters('amqp://root:root123456@127.0.0.1:5672')
connection = pika.BlockingConnection(parameters)
channel = connection.channel()

# channel.exchange_declare(exchange=exchange_name, exchange_type='fanout')  #定义一个exchange ,类型为fanout
# rest = channel.queue_declare(queue_name, exclusive=True)   #创建一个exclusive队列,并启用exchange
# channel.queue_bind(exchange=exchange_name, queue=queue_name, routing_key=queue_name)   #将随机队列名和exchange进行绑定


channel.basic_qos(prefetch_count = 1 )
channel.basic_consume(queue_name, callback, False)

# while True:
print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
    
