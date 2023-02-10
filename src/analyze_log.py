import csv
import sys

def analyze_log(path_to_file):
    print('path_to_file: ', path_to_file)

    try:
        if path_to_file[len(path_to_file) - 4:] != ".csv":
            raise FileNotFoundError("Extensão inválida: '{path_to_file}'")
        csv_list = ""
        with open(path_to_file, encoding= "utf-8") as file:
            csv_data = csv.DictReader(file, delimiter=",", quotechar='"')
            csv_list = list(csv_data)
            return write_txt(csv_list)

    except FileNotFoundError:
        print("Arquivo inexistente: '{path_to_file}'", file=sys.stderr)


def write_txt(param):
    with open("data/mkt_campaign.txt", "w") as file:
        for line in param:
            file.write(str(line) + "\n")
