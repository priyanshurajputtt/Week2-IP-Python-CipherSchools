# num=list(range(1,11))
# print(num)

# num.pop()
# print(num)

# print(num.index(2))


number=[1, 2, 3, 4, 5, 6, 7, 8, 9,1,5,9]
# print(number.index(1,5))


def nagative_list(l):
    nagative=[]
    for i in l:
        nagative.append(-i)
    return nagative

print(nagative_list(number))