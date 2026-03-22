import csv


class CSVReader:
    def read(self, file_path: str):
        rows = []
        with open(file_path, "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                rows.append(row)
        return rows