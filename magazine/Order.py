from magazine.utils import get_order_details, get_order_total_price


class Order:
    def __init__(self, order_id, product, quantity):
        self.order_id = order_id
        self.product = product
        self.quantity = quantity

    def get_total_price(self):
        return get_order_total_price(self)
