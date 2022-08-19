import csv


def file_check(path):
    if not path.endswith(".csv"):
        raise FileNotFoundError(f"Extensão inválida: '{path}")
    try:
        file = open(path)
        file.close()
    except FileNotFoundError:
        raise FileNotFoundError(f"Arquivo inexistente: '{path}")


def get_maria_favorite_dish(list):
    dish_dict = {order[1] for order in list}
    order_count = {dish: 0 for dish in dish_dict}

    for client, dish, weekday in list:
        if client == "maria":
            order_count[dish] += 1
    return max(order_count, key=order_count.get)


def analyze_log(path_to_file):
    file_check(path_to_file)

    with open(path_to_file) as csv_file:
        log_list = list(csv.reader(csv_file))
        maria_favorite_dish = get_maria_favorite_dish(log_list)
        arnaldo_hamburguer_count = 0
        joao_not_ordered = {order[1] for order in log_list}
        joao_absent_days = {order[2] for order in log_list}
        for client, dish, weekday in log_list:
            if client == "arnaldo" and dish == "hamburguer":
                arnaldo_hamburguer_count += 1
            elif client == "joao":
                joao_not_ordered.discard(dish)
                joao_absent_days.discard(weekday)

    with open("data/mkt_campaign.txt", mode="w") as file:
        file.write(
            f"{maria_favorite_dish}\n"
            f"{arnaldo_hamburguer_count}\n"
            f"{joao_not_ordered}\n"
            f"{joao_absent_days}\n"
        )
