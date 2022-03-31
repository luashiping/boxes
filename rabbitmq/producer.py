import time
import pika

parameters = pika.URLParameters('amqp://root:root123456@127.0.0.1:5672')
connection = pika.BlockingConnection(parameters)

channel = connection.channel()
queue_name="test"
exchange_name="amq.fanout"
arguments = {"ha-mode": "all"}

# channel.exchange_declare(exchange=exchange_name, durable=True)  #定义一个exchange ,类型为fanout
rest = channel.queue_declare(queue_name, durable=True, exclusive=False)   #创建一个exclusive队列,并启用exchange
channel.queue_bind(exchange=exchange_name, queue=queue_name, routing_key=queue_name)   #将随机队列名和exchange进行绑定

channel.queue_declare('test_2', durable=True, exclusive=False)   #创建一个exclusive队列,并启用exchange
channel.queue_bind(exchange=exchange_name, queue="test_2", routing_key="test_2")   #将随机队列名和exchange进行绑定

for i in range(100):
    channel.basic_publish(exchange=exchange_name, routing_key=queue_name, body='Hello World!')  #注意当未定义exchange时，routing_key需和queue的值保持一致
print('send success msg to rabbitmq')

# time.sleep(1000)
connection.close()   #关闭连接