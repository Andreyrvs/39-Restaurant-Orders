import csv


def analyze_log(path_to_file):
    print('path_to_file: ', path_to_file)

    if path_to_file[len(path_to_file) - 4:] != ".csv":
        raise FileNotFoundError(f"Extensão inválida: {path_to_file}")

    if path_to_file != "data/orders_1.csv":
        raise FileNotFoundError(f"Arquivo inexistente: {path_to_file}")

    read_csv(path_to_file)


def read_csv(path_to_file):

    with open(path_to_file, encoding="utf-8") as file:
        csv_data = csv.reader(file, delimiter=",", quotechar='"')
        csv_list = list(tuple(line) for line in csv_data)
        john_never_asked(csv_list)
        return csv_list


def write_txt(param):

    with open("data/mkt_campaign.txt", "w") as file:
        for line in param:
            file.write(str(line) + "\n")


def john_never_asked(list_tuple):
    dict_snacks = {}
    john_never_eaten = {}
    for a, b, c in list_tuple:
        if b not in dict_snacks:
            dict_snacks[b] = set()
        # if b not in dict_snacks:
        #     dict_snacks[a] = set()
        dict_snacks[b].add(a)
        # dict_snacks[a].add(b)
    
    print('dict_snacks: ', dict_snacks)
    
    # dict_values = dict_snacks.values()
    # pessoas = [item for item in dict_values]
    # print('pessoa: ', pessoas)
 
            
    return john_never_eaten
