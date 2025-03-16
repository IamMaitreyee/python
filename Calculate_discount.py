q=int(input("Enter the quantity: "))
p=q*100
print("Total price: ", p)
if p>=1000:
    d=p-p*(10/100)
    print("Price After Discount 10%: ", d)
else:
    print(p)