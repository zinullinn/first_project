quantity_text = "12"
price = 4.75

quantity = int(quantity_text)
whole_price = int(price)
total_text = str(quantity * price)

print(quantity, type(quantity).__name__)
print(whole_price, type(whole_price).__name__)
print(total_text, type(total_text).__name__)
