def get_order_total_price(order):
    return order.product.price * order.quantity


def get_product_details(product) -> str:
    return f"Product ID: {product.product_id}, Name: {product.name}, $: {product.price}"
