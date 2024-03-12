#!/usr/bin/env python3

class CashRegister:

    def __init__(self, discount=0):
        self.total = 0.0
        self.discount = discount
        self.items = []
        self.previous_transaction = []

    def add_item(self, title, price, quantity=1):
        self.total += price * quantity
        self.items.extend(([title] * quantity))
        self.previous_transaction.append(
            {'title': title, 'price': price, 'quantity': quantity}
            )

    def apply_discount(self):
        if self.discount:
            self.total = int(self.total - (self.discount/100 * self.total))
            print(f"After the discount, the total comes to ${self.total}.")
        else:
            print("There is no discount to apply.")

    def void_last_transaction(self):
        void_item = self.previous_transaction.pop()
        self.total = self.total - void_item['price'] * void_item['quantity']
