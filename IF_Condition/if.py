"""I am practicing my IF conditions"""

# n = int(input("Enter a number: "))
# print(n)
#
# message = "Number is even" if not n % 2 == 0 else "Number is odd"
# print(message)

# n = 8
#
# if n > 10 or n % 2 == 0:
#     print("Yay")
# else:
#     print("No")

indian = ["samosa", "daal", "naan"]
chinese = ["egg role", "pot sticker", "fried rice"]
italian = ["pizza", "pasta", "risotto"]

dish = input("Enter a dish: ").strip().lower()

if dish in indian:
    print(f"{dish} is indian")
elif dish in chinese:
    print(f" {dish} is chinese")
elif dish in italian:
    print(f"{dish} is italian")
else:
    print(f"Sorry, I don't know which cuisine {dish} belongs to.")
