def calculate_discount(price, discount_percent):
    if discount_percent>=20:
        discount=price * (discount_percent/100)
        final_price = price - discount
        return final_price
    else:
        return price

# Prompt the user for input
input_price=float(input("Please Input a Price:"))
input_discount=float(input("Please Input a Discount Percent:"))

# Calculate the final price
final_price=calculate_discount(input_price,input_discount)

# Print the appropriate message
if input_discount >= 20:
    print(f"Discount applied! Final price: ${final_price:.2f}")
else:
    print(f"No discount applied. Original price remains: ${final_price:.2f}")
