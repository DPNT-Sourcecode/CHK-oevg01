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
                # Check if count of items matches free item special
                if isinstance(special, tuple):
                    if sku in counter and counter[sku]>=num_items:
                        free_sku = special[0]
                        num_free_sku = special[1]
                        if free_sku in counter:
                            free_items = (counter[sku]//num_items)*num_free_sku
                            counter[free_sku]-=free_items

        total = 0
        for sku, items in counter.items():
            # skip neg or 0 item counts - indicates free sku
            if items<1:
                continue
            sku_price = CheckoutSolution.PRICING[sku]
            if sku in CheckoutSolution.SPECIALS:
                specials = CheckoutSolution.SPECIALS[sku]
                ordered_offers = sorted(specials.keys(), reverse=True)
                for special_num_items, special_value in ordered_offers.items():
                    if items>=special_num_items and not isinstance(special_value, tuple):
                        special_price = (items//special_num_items)*special_value
                        items = items % special_num_items
                        total+=special_price
                rem_price = items * sku_price
                total += rem_price
            else:
                total+= sku_price*items
        return total


