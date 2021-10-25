
import unittest
import surfshop
class SystemTest(unittest.TestCase):
  def setUp(self):
    self.cart = surfshop.ShoppingCart()
    
  def test_add_surfboards_with_board_one_return_message(self):
    expected_message = 'Successfully added 1 surfboard to cart!'
    message = self.cart.add_surfboards()
    self.assertEqual(message, expected_message)

  def test_add_more_surfboards(self):
      num_surfboards = [2, 3, 4]
      for num in num_surfboards:
        self.cart = surfshop.ShoppingCart()
        with self.subTest(num):
          self.assertEqual(self.cart.add_surfboards(num), f'Successfully added {num} surfboards to cart!', "Check adding surfboards to a cart")

  def test_add_surfboards_with_board_two_return_message(self):
    expected_message = 'Successfully added 2 surfboards to cart!'
    message = self.cart.add_surfboards(2)
    self.assertEqual(message, expected_message)

  def test_add_surfboards_with_board_five_raises_error(self):
    expected_exception = surfshop.TooManyBoardsError
    expected_message = 'Cart cannot have more than 4 surfboards in it!'
    with self.assertRaises(expected_exception) as ex:
        self.cart.add_surfboards(5)
        self.assertEqual(expected_message, str(ex.exception))

  def test_apply_locals_discount_with_value_true_returns_true(self):
     self.cart.apply_locals_discount()
     bool_val = self.cart.locals_discount
     self.assertTrue(bool_val)

  def test_set_checkout_date_with_invalid_date_raises_error(self):
    from datetime import datetime
    date = datetime.strptime('Jun 1 2005  1:33PM', '%b %d %Y %I:%M%p')
    expected_error = surfshop.CheckoutDateError
    with self.assertRaises(expected_error):
      self.cart.set_checkout_date(date)

unittest.main()
