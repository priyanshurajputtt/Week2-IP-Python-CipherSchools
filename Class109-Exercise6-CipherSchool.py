num=[1,2,3,[1,2],[3,4]]

def list_count(l):
    count=0
    for i in l:
        if type(i)==list:
            count+=1
    return count
print(list_count(num))