from collections import Counter

class CheckoutSolution:
    PRICING = {
        'A': 50,
        'B': 30,
        'C': 20,
        'D': 15,
        'E': 40,
        'F': 10,
        'G': 20,
        'H': 10,
        'I': 35,
        'J': 60,
        'K': 70,
        'L': 90,
        'M': 15,
        'N': 40,
        'O': 10,
        'P': 50,
        'Q': 30,
        'R': 50,
        'S': 20,
        'T': 20,
        'U': 40,
        'V': 50,
        'W': 20,
        'X': 17,
        'Y': 20,
        'Z': 21
    }


    SPECIALS = {
        'A': { 3: 130, 5: 200 },
        'B': { 2: 45 },
        'E': { 2: ('B', 1) },
        'F': { 2: ('F', 1) },
        'H': { 5: 45, 10: 80 },
        'K': { 2: 120 },
        'N': { 3: ('M', 1) },
        'P': { 5: 200 },
        'Q': { 3: 80 },
        'R': { 3: ('Q', 1) },
        'U': { 3: ('U', 1) },
        'V': { 2: 90, 3: 130}
    }

    GROUP_SPECIALS = {
        ('S','T','X','Y','Z'): (3, 45)
    }

    # skus = unicode string
    def checkout(self, skus):
        if skus=="":
            return 0

        for sku in skus:
            if sku not in CheckoutSolution.PRICING:
                return -1

        total = 0
        counter = Counter(skus)

        # Count total for group specials. Sum special offers and remove from items
        for group, special in CheckoutSolution.GROUP_SPECIALS.items():
            special_items=special[0]
            special_price=special[1]

            # Keep track of all items part of this group
            groups_counted=[]
            for sku in group:
                if sku in counter:
                    # add full count of items to list
                    groups_counted.extend([sku]*counter[sku])

            # Sort by highest prices to remove those first
            groups_counted.sort(key=lambda sku: CheckoutSolution.PRICING[sku], reverse=True)

            group_items = len(groups_counted)
            num_group_specials = group_items//special_items

            total+= num_group_specials*special_price

            # Deduct sku count for all items used in group special
            items_used = num_group_specials*special_items
            for i in range(items_used):
                sku=groups_counted[i]
                counter[sku]-=1

        # Remove free items from specials
        for sku, specials in CheckoutSolution.SPECIALS.items():
            ordered_offers = sorted(specials.items(), reverse=True)
            for num_items, special in ordered_offers:
                # Check if count of items matches free item special
                if isinstance(special, tuple):
                    if sku in counter and counter[sku]>=num_items:
                        free_sku = special[0]
                        num_free_sku = special[1]
                        if free_sku in counter:
                            free_items = 0
                            if free_sku==sku:
                                tmp_count = counter[free_sku]
                                while tmp_count > num_items:
                                    tmp_count-=num_items+num_free_sku
                                    free_items+=num_free_sku
                            else:
                                free_items = (counter[sku] // num_items) * num_free_sku
                            counter[free_sku] -= free_items

        # Sum total items with discounts if applicable
        for sku, items in counter.items():
            # skip neg or 0 item counts - indicates free sku
            if items<1:
                continue
            sku_price = CheckoutSolution.PRICING[sku]
            if sku in CheckoutSolution.SPECIALS:
                specials = CheckoutSolution.SPECIALS[sku]
                ordered_offers = sorted(specials.items(), reverse=True)
                for special_num_items, special_value in ordered_offers:
                    if items>=special_num_items and not isinstance(special_value, tuple):
                        special_price = (items//special_num_items)*special_value
                        items = items % special_num_items
                        total+=special_price
                rem_price = items * sku_price
                total += rem_price
            else:
                total+= sku_price*items
        return total