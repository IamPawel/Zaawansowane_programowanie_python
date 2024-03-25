form magzaine.utils import order_details

class Order:
    def __init__(self, order_id, price):
        self.order_id = order_id
        self.price = price

    def __str__(self):
        return order_details
    def order_details(self):
        return order_details(self)