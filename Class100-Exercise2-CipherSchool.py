num=[1,2,3,4]


# reverse method

# def reverse_list(l):
#     l.reverse()
#     return l
# print(reverse_list(num))



# pop method

# def reverse_list(l):
#     return l[::-1]
# print(reverse_list(num))



# pop/append method
def reverse_list(l):
    r_list = []
    for i in range(len(l)):
        popped_item= l.pop()
        r_list.append(popped_item)
    return r_list
print(reverse_list(num))