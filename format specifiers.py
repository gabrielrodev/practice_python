# format specifiers = {value:flags} format a value based on what flags are inserted

# .(number)f = round to that many decimal places (fixed point)
# :(number) = allocate that many spaces (basically gives spaces in between if you do something like{value:10})
# :03 = allocate and zero pad that many spaces (ok instead of just leaving space as the flag above it leaves 0)
# :< = left justify
# :> = right justify
# :^ = center align (I think this is for like text alignment)
# :+ = use a plus sign to indicate positive value (it shoes which on is positive and which one is negative)
# := = place sign to leftmost position
# :  = insert a space before positive numbers (this could be use to align the negative values with the positives)
# :, = comma separator (is neat to make numbers have comas and look better)


price1 = 3000.14159
price2 = -9870.65
price3 = 1200.34

print(f"Price 1 is ${price1:+,.1f}")
print(f"Price 2 is ${price2:+,.1f}")
print(f"Price 3 is ${price3:+,.1f}")