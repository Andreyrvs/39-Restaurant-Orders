import csv
from collections import Counter


def analyze_log(path_to_file):
    print('path_to_file: ', path_to_file)
    verify_dot_csv(path_to_file)


    readed_file = read_csv(path_to_file)
    maria = most_frequency_order(readed_file, 'maria')
    arnaldo = counter_order(readed_file, 'arnaldo', 'hamburguer')
    john_asked = john_never_asked(readed_file, 'joao')
    john_has_never = john_has_never_been(readed_file, 'joao')
    write_this_list = [maria, arnaldo, john_asked, john_has_never]
    write_txt(write_this_list)


def verify_dot_csv(path_to_file):
    if path_to_file[len(path_to_file) - 4:] != ".csv":
        raise FileNotFoundError(f"Extensão inválida: {path_to_file}")

    if path_to_file != "data/orders_1.csv":
        raise FileNotFoundError(f"Arquivo inexistente: {path_to_file}")


def read_csv(path_to_file):

    with open(path_to_file, encoding="utf-8") as file:
        headerList = ['client', 'order', 'day']
        file_list = csv.DictReader(file, fieldnames=headerList)
        return [each_order for each_order in file_list]


def write_txt(list_test):

    with open("data/mkt_campaign.txt", "w") as file:
        for line in list_test:
            print('line: ', line)
            file.write(
                f"{line}\n"
            )


def most_frequency_order(readed_file, name):
    frequency_order = {}

    for order in readed_file:
        if order['client'] == name:
            order_name = order['order']
            frequency_order[order_name] = frequency_order.get(order_name, 0) + 1

    most_requested = max(frequency_order, key=frequency_order.get)
    return most_requested


        


def counter_order(readed_file, name, order):
    counter = 0
    for orders in readed_file:
        if orders['client'] == name and orders['order'] == order:
            counter += 1
    return counter


def john_never_asked(readed_file, name):
    all_dishes = set()
    john_request = set()
    for all_orders in readed_file:
        all_dishes.add(all_orders['order'])
        if all_orders['client'] == name:
            john_request.add(all_orders['order'])
    never_asked = all_dishes.difference(john_request)
    return never_asked


def john_has_never_been(readed_file, name):
    snack_bar_open = set()
    john_goes_that_day = set()

    for all_orders in readed_file:
        snack_bar_open.add(all_orders['day'])
        if all_orders['client'] == name:
            john_goes_that_day.add(all_orders['day'])
    did_not_enter = snack_bar_open.difference(john_goes_that_day)
    return did_not_enter

