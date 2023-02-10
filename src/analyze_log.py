import csv
import sys

def analyze_log(path_to_file):
    print('path_to_file: ', path_to_file)
    if path_to_file != "data/orders_1.csv":
        raise FileNotFoundError("Arquivo inexistente: '{path_to_file}'")

    if path_to_file[len(path_to_file) - 4:] != ".csv":
        return print("Extensão inválida: '{path_to_file}'", file=sys.stderr)

    with open(path_to_file, encoding= "utf-8") as file:
        csv_data = csv.DictReader(file, delimiter=",", quotechar='"')
        csv_list = list(csv_data)
            # print(csv_list)