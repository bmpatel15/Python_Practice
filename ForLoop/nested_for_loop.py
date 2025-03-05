products = ["iPhone", "MacBook", "iPad", "Apple Watch"]
regions = ["US", "China", "India"]
revenue = [420, 100, 150, 30, 20, 10, 50, 100, 200, 300, 400, 500]

i = 0

for product in products:
    for region in regions:
        rev = revenue[i]
        i = i + 1
        print(f"{product} {region} revenue: ", rev)
