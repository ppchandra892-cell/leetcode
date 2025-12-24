# Shuffle the Array
nums=[2,5,1,3,4,7,6,3,6,9,2,3] 
final_list=[]
if len(nums)%2!=0:
    print("Invalid Length of List")
else:
    li_len=len(nums)//2
    # print(li_len)
    x=nums[0:li_len]
    y=nums[li_len:]
    print(x)
    print(y)
    for i in range(li_len):
        final_list.append(x[i])
        final_list.append(y[i])
    print("Shuffles List",final_list)