class ShopItem:
    def __init__(self, name, weight, price):
        self.name = name
        self.weight = weight
        self.price = price

    def __hash__(self):
        return hash((self.name.lower(), self.weight, self.price))

    def __eq__(self, other):
        return self.self.name.lower() == other.name.lower() \
            and self.weight == other.weight and self.price == other.price
lst_in = list(map(str.strip, sys.stdin.readlines()))