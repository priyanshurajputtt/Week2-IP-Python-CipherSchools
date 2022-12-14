str=['abc','tuv','xyz']
def reverse_list(l):
    list = []
    for i in l:
        list.append(i[::-1])
    return list
print(reverse_list(str))