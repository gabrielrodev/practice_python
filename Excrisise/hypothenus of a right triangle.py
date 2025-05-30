import math
a = float(input("Enter the short side:"))
b = float(input("Enter the long side:"))


hypothenus = math.sqrt(pow(a,2)+ pow(b,2))

print(f"This is the hypothenus:{round(hypothenus,2)}")