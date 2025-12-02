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
        for sku in skus:
            if sku not in CheckoutSolution.PRICING:
                return -1

        counter = Counter(skus)
        total = 0
        for sku, items in counter.items():
            sku_price = CheckoutSolution.PRICING[sku]
            if sku in CheckoutSolution.SPECIALS and items>=CheckoutSolution.SPECIALS[sku].num_items:
                special = CheckoutSolution.SPECIALS[sku]
                special_price = (items//special.num_items)*special.price
                rem_price = (items % special.num_items)*sku_price
                total+=special_price+rem_price
            else:
                total+= sku_price*items
        return total
