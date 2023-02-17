class TrackOrders:
    def __init__(self):
        self._orders = list()

    def __len__(self):
        return len(self._orders)

    def add_new_order(self, customer, order, day):
        new_order = self._orders.append(
            {'customer': customer, 'order': order, 'day': day}
        )
        return new_order

    def get_most_ordered_dish_per_customer(self, customer):
        print('customer: ', customer, self._orders)
        all_orders = set()
        customer_orders = set()

        for order in self._orders:
            order = order['order']
            all_orders.add(order)

            if order['customer'] == customer:
                customer_orders.add(order)

        pratos_nao_pedidos = all_orders - customer_orders
        return pratos_nao_pedidos

    def get_never_ordered_per_customer(self, customer):
        pass

    def get_days_never_visited_per_customer(self, customer):
        pass

    def get_busiest_day(self):
        pass

    def get_least_busy_day(self):
        pass
