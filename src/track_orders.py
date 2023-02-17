class TrackOrders:
    def __init__(self):
        self.orders = list()

    def __len__(self):
        return len(self.orders)

    def add_new_order(self, customer, order, day):
        new_order = self.orders.append(
            {'customer': customer, 'order': order, 'day': day}
        )
        return new_order

    def get_most_ordered_dish_per_customer(self, customer):
        customer_orders = [
            order['order']
            for order in self.orders
            if order['customer'] == customer
        ]

        print(set(customer_orders))
        return max(set(customer_orders), key=customer_orders.count)

    def get_never_ordered_per_customer(self, customer):
        all_dishes = set()
        customer_order = set()

        for order in self.orders:
            dishes = order['order']
            all_dishes.add(dishes)

            if order['customer'] == customer:
                customer_order.add(dishes)

        pratos_nao_pedidos = all_dishes - customer_order
        return pratos_nao_pedidos

    def get_days_never_visited_per_customer(self, customer):
        all_days = set(order['day'] for order in self.orders)
        days_visited = set(
            order['day']
            for order in self.orders
            if order['customer'] == customer
        )
        days_not_visited = all_days - days_visited
        return days_not_visited

    def get_busiest_day(self):
        days = [order['day'] for order in self.orders]
        busiest_day = max(set(days), key=days.count)
        return busiest_day

    def get_least_busy_day(self):
        days = [order['day'] for order in self.orders]
        busiest_day = min(set(days), key=days.count)
        return busiest_day
