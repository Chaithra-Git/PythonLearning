sales = [40,45,33,38,37,20]
months = ["Jan", "Feb", "Mar", "Apr", "May"]
threshold = 35

for  monthly_sales, month in zip(sales,months):
    if monthly_sales < threshold:
        print(f"{monthly_sales} is less than threshold in {month}")
        break

    else:
        print(f"{monthly_sales} is more than threshold {month}")
