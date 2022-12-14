# # function practice
def last_char(name):
    return name[-1]
print(last_char("aaryan"))

def odd_even(num):
    if num%2==0:
        return "even"
    else:
        return "odd"

def odd_even(num):
    if num%2==0:
        return "even"
    return "odd"

print(odd_even(11))

def is_even(num):
    if num%2==0:
        return True
    return False
print(is_even(456))

def is_even(num):
    return num%2==0
print(is_even(45))


def song():
    return "happy birthday song"
print(song())