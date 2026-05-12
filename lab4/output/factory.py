from output.console_strategy import ConsoleOutputStrategy
from output.kafka_strategy import KafkaOutputStrategy


class OutputFactory:
    @staticmethod
    def create_output_strategy(config):
        output_type = config["output"]["type"]

        if output_type == "console":
            return ConsoleOutputStrategy()

        if output_type == "kafka":
            return KafkaOutputStrategy(
                bootstrap_servers=config["kafka"]["bootstrap_servers"],
                topic=config["kafka"]["topic"]
            )

        raise ValueError("Невідомий тип виводу")