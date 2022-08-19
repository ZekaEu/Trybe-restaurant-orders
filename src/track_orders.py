from collections import Counter


class TrackOrders:
    def __init__(self):
        self.orders = []

    def __len__(self):
        return len(self.orders)

    def add_new_order(self, customer, order, day):
        new_order = (customer, order, day)
        self.orders.append(new_order)

    def get_most_ordered_dish_per_customer(self, customer):
        order_count = {order[1]: 0 for order in self.orders}
        for client, dish, _ in self.orders:
            if client == customer:
                order_count[dish] += 1
        return max(order_count, key=order_count.get)

    def get_never_ordered_per_customer(self, customer):
        pass

    def get_days_never_visited_per_customer(self, customer):
        pass

    def get_busiest_day(self):
        return Counter([ordr[2] for ordr in self.orders]).most_common(1)[0][0]

    def get_least_busy_day(self):
        return Counter([ordr[2] for ordr in self.orders]).most_common()[-1][0]
