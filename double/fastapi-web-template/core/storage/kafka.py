import asyncio
import json
import logging

from aiokafka import AIOKafkaProducer, AIOKafkaConsumer

from core.config.common import config
from core.middleware import g


logger = logging.getLogger(__name__)


class MyKafka:
    producer: AIOKafkaProducer
    consumer: AIOKafkaConsumer

    def __init__(self):
        loop = asyncio.get_event_loop()
        self.producer = AIOKafkaProducer(
            loop=loop, bootstrap_servers=config.KAFKA_BOOTSTRAP_SERVERS
        )
        self.consumer = AIOKafkaConsumer(
            config.KAFKA_TOPIC,
            loop=loop,
            bootstrap_servers=config.KAFKA_BOOTSTRAP_SERVERS,
        )
        self.start_consumer()
        self.start_producer()

    def start_producer(self):
        self.producer.start()

    def start_consumer(self):
        self.consumer.start()

    def send(self, data):
        self.producer.send(config.KAFKA_TOPIC, json.dumps(data))


# kafka = MyKafka()
