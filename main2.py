# TODO импортировать необходимые молули
import json
import csv

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    with open(INPUT_FILENAME, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file, delimiter=',', lineterminator='\n')
        data = [row for row in reader]

    with open(OUTPUT_FILENAME, mode='w', encoding='utf-8') as output_file:
        json.dump(data, output_file, indent=4, ensure_ascii=False)
if __name__ == '__main__':
    task()
    with open(OUTPUT_FILENAME, mode='r', encoding='utf-8') as output_f:
        for line in output_f:
            print(line, end='')


