user_info= {
    'name': 'Aaryan',
    'age' : '18',
}

# add Data 
user_info['fav_song']=['song1',]

print(user_info)

# # pop method
# popped_item=user_info.pop('fav_song')
# print(f"popped_item is {popped_item}")
# print(user_info)


# popitem method
popped_item=user_info.popitem()
print(popped_item)
print(user_info)