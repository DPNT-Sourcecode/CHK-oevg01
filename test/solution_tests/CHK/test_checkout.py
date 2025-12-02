from solutions.CHK.checkout_solution import CheckoutSolution

class TestCheckout:
    def test_simple_checkout(self):
        assert CheckoutSolution().checkout('A') == 50

    def test_free_item_checkout(self):
        assert CheckoutSolution().checkout('EEB') == 80