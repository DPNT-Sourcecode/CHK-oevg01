from solutions.CHK.checkout_solution import CheckoutSolution

class TestCheckout:
    def test_missing_checkout(self):
        assert CheckoutSolution().checkout('') == 0

    def test_not_sku_checkout(self):
        assert CheckoutSolution().checkout('1') == -1

    def test_simple_checkout(self):
        assert CheckoutSolution().checkout('A') == 50

    def test_free_item_checkout(self):
        assert CheckoutSolution().checkout('EEB') == 80

    def test_free_item_with_discount_checkout(self):
        assert CheckoutSolution().checkout('EEBBB') == 125

    def test_free_items_no_pay_checkout(self):
        assert CheckoutSolution().checkout('EEEEEEBB') == 240

    def test_same_free_item_checkout(self):
        assert CheckoutSolution().checkout('FF') == 20
        assert CheckoutSolution().checkout('FFFF') == 30
        assert CheckoutSolution().checkout('FFFFFF') == 40

    def test_group_special_checkout(self):
        assert CheckoutSolution().checkout('XYZ') == 45
        # Remove higher prices first, i.e. Z&Y discounts, with X remainder
        assert CheckoutSolution().checkout('ZZYX') == 62
        assert CheckoutSolution().checkout('XXYYZZ') == 90