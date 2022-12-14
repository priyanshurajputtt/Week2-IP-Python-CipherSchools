num=[1,2,3,4,5,6,7,8,9]
def filter_list(l):
    odd=[]
    even=[]
    for i in l:
        if i%2==0:
            even.append(i)
        else:
            odd.append(i)
    output=[odd,even]
    return output
print(filter_list(num))  
        