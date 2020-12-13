from pykafka import KafkaClient

# kafka producer

client = KafkaClient(hosts="localhost:9092")
topic = client.topics['testBusdata']
producer = topic.get_sync_producer()

count = 1
while True:
    message = ("hello-" + str(count)).encode('ascii')
    producer.produce(message)
    print(message)
    count = count + 1