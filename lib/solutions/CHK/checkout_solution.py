from collections import Counter

class Special:
    def __init__(self, num_items, price):
        self.num_items = num_items
        self.price = price

class CheckoutSolution:
    PRICING = {
        'A': 50,
        'B': 30,
        'C': 20,
        'D': 15
    }

    SPECIALS = {
        'A': Special(3, 130),
        'B': Special(3, 130)
    }

    # skus = unicode string
    def checkout(self, skus):
        
