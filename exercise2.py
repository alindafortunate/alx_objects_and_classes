# Exercise 2: Creating a Product Catalog

# Instruction:

# Define a Product class with attributes like name, price, and quantity.
# Implement a method to calculate the total value of products in stock.


class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def total_value(self):

        if self.quantity > 1:
            total_value = self.price * self.quantity
            return f"The total value of {self.quantity} {self.name}s is: {total_value}"
        else:
            return f"The value of {self.quantity} {self.name} is: {self.price}"


stock_January = Product("Mango", 1000, 10)
print(stock_January.total_value())
stock_February = Product("orange", 2000, 1)
print(stock_February.total_value())
