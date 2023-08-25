#!/usr/bin/env python3

from cash_register import CashRegister

import io
import sys

class TestCashRegister:
    '''CashRegister in cash_register.py'''

    cash_register = CashRegister()
    cash_register_with_discount = CashRegister(20)

    def reset_register_totals(self):
        self.cash_register.total = 0
        self.cash_register_with_discount.total = 0

    def test_discount_attribute(self):
        '''takes one optional argument, a discount, on initialization.'''
        assert(self.cash_register.discount == 0)
        assert(self.cash_register_with_discount.discount == 20)

    # ... (other test methods)

    def test_void_last_transaction(self):
        '''subtracts the last item from the total'''
        self.cash_register.add_item("apple", 0.99)
        self.cash_register.add_item("tomato", 1.76)
        self.cash_register.void_last_transaction()
        assert(self.cash_register.total == 0.99)
        self.reset_register_totals()

    def test_void_last_transaction_with_multiples(self):
        '''returns the total to 0.0 if all items have been removed'''
        self.cash_register.add_item("tomato", 1.76, 2)
        self.cash_register.void_last_transaction()
        self.cash_register.void_last_transaction()  # Void the last transaction again
        assert self.cash_register.total == 0.0
        self.reset_register_totals()
