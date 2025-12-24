# Richest Customer Wealth
accounts=[[1,2,3],
        [3, 2, 1]] 
sum_=[]

for i in accounts:
    sum_.append(sum(i))
richest_wealth=max(sum_)
print("Customer Wealth",richest_wealth)