from collections import Counter

class CheckoutSolution:
    PRICING = {
        'A': 50,
        'B': 30,
        'C': 20,
        'D': 15
    }

    SPECIALS = {
        'A': { 3: 130, 5: 200 },
        'B': { 2: 45 }
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
            if sku in CheckoutSolution.SPECIALS:
                specials = CheckoutSolution.SPECIALS[sku]
                ordered_offers = sorted(specials.keys(), reverse=True)
                for special in ordered_offers:
                    if items>=special.num_items:
                        special_price = (items//special.num_items)*special.price
                        items = items % special.num_items
                        total+=special_price
                rem_price = items * sku_price
                total += rem_price
            else:
                total+= sku_price*items
        return total