"""
Stworzyć funkcję, która przyjmie 3 argumenty typu int i sprawdzi czy suma
dwóch pierwszych liczb jest większa lub równa trzeciej, a następnie zwróci tę
informację jako typ logiczny bool
"""


def check(a: int, b: int, c: int):
    if a + b >= c:
        return True
    else:
        return False


check1 = check(2, 3, 5)
print(check1)
