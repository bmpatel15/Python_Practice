monthly_sales = [42, 38, 33, 38,40, 45]
month = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
threshold = 35

for sales_amount, month in zip(monthly_sales, month):
    if sales_amount < threshold:
        print(f"Sales amount {sales_amount} is less than threshold in {month}")
        break
    else:
        print(f"Sales amount {sales_amount} is greater than threshold in {month}")
