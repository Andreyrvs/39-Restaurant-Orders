import csv


def analyze_log(path_to_file):
    print('path_to_file: ', path_to_file)

    if path_to_file[len(path_to_file) - 4:] != ".csv":
        raise FileNotFoundError(f"Extensão inválida: {path_to_file}")

    if path_to_file != "data/orders_1.csv":
        raise FileNotFoundError(f"Arquivo inexistente: {path_to_file}")

    readed_file = read_csv(path_to_file)
    john_asked = john_never_asked(readed_file, 'joao')
    john_has_never = john_has_never_been(readed_file, 'joao')
    write_this_list = [john_asked, john_has_never]
    write_txt(write_this_list)

def read_csv(path_to_file):

    with open(path_to_file, encoding="utf-8") as file:
        headerList = ['cliente', 'pedido', 'dia']
        file_list = csv.DictReader(file, fieldnames=headerList)
        return [each_order for each_order in file_list]
        


def write_txt(list_test):

    with open("data/mkt_campaign.txt", "w") as file:
        for line in list_test:
            print('line: ', line)
            file.write(
                f"{line}\n"
            )


def john_never_asked(list_of_orders, name):
    all_dishes = set()
    john_request = set()
    for all_orders in list_of_orders:
        all_dishes.add(all_orders['pedido'])
        if all_orders['cliente'] == name:
            john_request.add(all_orders['pedido'])
    never_asked = all_dishes.difference(john_request)
    return never_asked


def john_has_never_been(list_of_orders, name):
    snack_bar_open = set()
    john_goes_that_day = set()

    for all_orders in list_of_orders:
        snack_bar_open.add(all_orders['dia'])
        if all_orders['cliente'] == name:
            john_goes_that_day.add(all_orders['dia'])
    did_not_enter = snack_bar_open.difference(john_goes_that_day)
    return did_not_enter