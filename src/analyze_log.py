import csv
import sys


def analyze_log(path_to_file):
    print('path_to_file: ', path_to_file)

    if path_to_file[len(path_to_file) - 4:] != ".csv":
        raise FileNotFoundError(f"Extensão inválida: {path_to_file}")
    try:
        read_csv(path_to_file)

    except FileNotFoundError:
        raise FileNotFoundError(f"Arquivo inexistente: {path_to_file}")


def read_csv(path_to_file):

    with open(path_to_file, encoding="utf-8") as file:
        csv_data = csv.DictReader(file, delimiter=",", quotechar='"')
        csv_list = list(csv_data)
        return write_txt(csv_list)


def write_txt(param):

    with open("data/mkt_campaign.txt", "w") as file:
        for line in param:
            file.write(str(line) + "\n")
