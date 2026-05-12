import yaml

from readers.file_reader import FileReader
from output.factory import OutputFactory


def load_config():
    with open("config.yaml", "r", encoding="utf-8") as file:
        return yaml.safe_load(file)


def main():
    config = load_config()

    reader = FileReader("data.txt")
    lines = reader.read_lines()

    output_strategy = OutputFactory.create_output_strategy(config)

    for line in lines:
        output_strategy.output(line)


if __name__ == "__main__":
    main()