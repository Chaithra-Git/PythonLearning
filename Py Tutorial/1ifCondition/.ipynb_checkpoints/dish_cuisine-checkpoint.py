indian = {'samosa', 'pani puri', 'sambar'}
chinese = {'noodles', 'pho', 'fried rice'}

dish = input("Enter the dish: ")

if dish in indian:
    print(f"{dish} is Indian")
elif dish in chinese:
    print(f"{dish} is Chinese")
else:
    print("I dont know")