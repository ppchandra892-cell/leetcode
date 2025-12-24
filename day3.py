# Day-3-----Multi-User Shopping Cart Billing
n=[[100,400,127],
[450,600],
[127,128,57,600],[0,1,6/900],[2500,2500]
]
output=[]
for i in n:
    total=sum(i)
    if total>0 and total<500:
        output.append(total)
    elif total>500 and total<1000:
        discount=total/100*5
        total_price=total-discount
        output.append(total_price)
    elif total>1000 and total<5000:
        discount1=total/100*15
        total_price=total-discount1
        output.append(total_price)
    elif total>=5000:
        discount2=total/100*20
        total_price=total-discount2
        output.append(total_price)
    else:
        print("none")
print(output)