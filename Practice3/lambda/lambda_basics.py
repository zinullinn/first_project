"""A lambda function for a short calculation."""

# Here is a lambda that calculates the price after a discount.
apply_discount = lambda price, percent: price * (1 - percent / 100)

print(apply_discount(10000, 15))
