#“Longest Subarray with Equal 0s and 1s”
nums = [1,0,0,1,1]
one=nums.count(1)
# print(one)
zero=nums.count(0)
# print(zero)
minimum=min(one,zero)*2
print(minimum)

