products = ["iphone","ipad","mac"]
regions=["india","usa","china"]
revenue=[20,25,21,23,34,35,67,90,78]
i=0
for product in products:
    for region in regions:
        region_revenue = revenue[i]
        i += 1
        print(f"{product} {region} {region_revenue}")