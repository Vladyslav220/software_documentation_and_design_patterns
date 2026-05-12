from kafka import KafkaProducer
from output.output_strategy import OutputStrategy


class KafkaOutputStrategy(OutputStrategy):
    def __init__(self, bootstrap_servers, topic):
        self.topic = topic
        self.producer = KafkaProducer(
            bootstrap_servers=bootstrap_servers,
            value_serializer=lambda value: value.encode("utf-8")
        )

    def output(self, message):
        self.producer.send(self.topic, message.strip())
        self.producer.flush()