# TODO импортировать необходимые молули
import csv
import json
import pprint

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task(f_csv, f_json) -> None:
    file_csv = open(INPUT_FILENAME, 'r')
    reader = csv.DictReader(file_csv)
    # TODO считать содержимое csv файла

    file_json = open(OUTPUT_FILENAME, 'w')
    list_ = []

    for row in reader:
        json.dump(row, file_json, indent=4)
        file_json.write('\n')
        list_.append(row)
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(list_)# TODO Сериализовать в файл с отступами равными 4


if __name__ == '__main__':
    # Нужно для проверки
    task(INPUT_FILENAME, OUTPUT_FILENAME)

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
