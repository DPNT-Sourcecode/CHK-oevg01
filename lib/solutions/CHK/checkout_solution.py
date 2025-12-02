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
        'B': { 2: 45 },
        'E': { 2: ('B', 1) }
    }



    # skus = unicode string
    def checkout(self, skus):
        for sku in skus:
            if sku not in CheckoutSolution.PRICING:
                return -1

        counter = Counter(skus)
        for sku, specials in CheckoutSolution.SPECIALS:
            for num_items, special in specials:
                if isinstance(special, tuple) and counter[sku]>=num_items:
                    if
                    free_items = counter[sku]//num_items
                    counter[sku]-=free_items

        total = 0
        for sku, items in counter.items():
            sku_price = CheckoutSolution.PRICING[sku]
            if sku in CheckoutSolution.SPECIALS:
                specials = CheckoutSolution.SPECIALS[sku]
                ordered_offers = sorted(specials.keys(), reverse=True)
                for special_num_items, special_value in ordered_offers.items():
                    if items>=special_num_items:
                        if not isinstance(special_value, tuple):
                            special_price = (items//special_num_items)*special_value
                            items = items % special_num_items
                            total+=special_price
                rem_price = items * sku_price
                total += rem_price
            else:
                total+= sku_price*items
        return total

