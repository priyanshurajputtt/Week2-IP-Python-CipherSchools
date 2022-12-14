list1=[1,2,5,8]
list2=[1,2,7,6]

def common_list(list1,list2):
    common = []
    for i in list1:
        if i in list2:
            common.append(i)            
    return common
print(common_list(list1,list2))