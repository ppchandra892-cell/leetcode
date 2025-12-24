# Day-4----Running Maximum Filter

N = [1,2,1,3,4,5,6,7,8,9,2,1,5,6,10]
result = []
Max = 0
for x in N:
    if x >= Max:
        result.append(x)
        Max = x   
print(result)