import csv


def analyze_log(path_to_file):
    print('path_to_file: ', path_to_file)

    if path_to_file[len(path_to_file) - 4:] != ".csv":
        raise FileNotFoundError(f"Extensão inválida: {path_to_file}")

    if path_to_file != "data/orders_1.csv":
        raise FileNotFoundError(f"Arquivo inexistente: {path_to_file}")

    # joao_days = days_never_gone(read_csv(path_to_file), 'joao')
    read_csv(path_to_file)


def read_csv(path_to_file):

    with open(path_to_file, encoding="utf-8") as file:
        headerList = ['cliente', 'pedido', 'dia']
        file_list = csv.DictReader(file, fieldnames=headerList)
        return [each_order for each_order in file_list]
        


def write_txt(param):

    with open("data/mkt_campaign.txt", "w") as file:
        for line in param:
            file.write(str(line) + "\n")


def john_never_asked(list_of_orders, name):
    all_dishes = set()
    joao_order = set()
    for all_orders in list_of_orders:
        all_dishes.add(all_orders['pedido'])
        # print(all_orders['pedido'])
        # print(all_dishes)
        if all_orders['cliente'] == name:
            joao_order.add(all_orders['pedido'])
    order_never_made = all_dishes.difference(joao_order)
    return order_never_made
