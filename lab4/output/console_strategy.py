from output.output_strategy import OutputStrategy


class ConsoleOutputStrategy(OutputStrategy):
    def output(self, message):
        print(message.strip())