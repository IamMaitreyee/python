p=int(input("Enter the price of bike: "))
if p>=100000:
    d=p-p*(15/100)
    print("Price After Discount 15%: ", d)
elif p>50000 and p<100000:
    d = p - p * (10 / 100)
    print("Price After Discount 10%: ", d)
elif p<=50000:
    d = p - p * (5 / 100)
    print("Price After Discount 5%: ", d)
else:
    print(p)