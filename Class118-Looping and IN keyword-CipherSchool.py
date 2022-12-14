user_info= {
    'name': 'Aaryan',
    'age' : '18',
}
# if 'name' in user_info:
# if 'surname' in user_info:
# if 'Aaryan in user_info.values():
#     print('present')
# else:
#     print('not present')


# loop
# for i in user_info:
#     print(i)

# for i in user_info:
#     print(user_info[i])
# for i in user_info.values():
#     print(i)


# value method
# user_info_value=user_info.values()
# print(user_info_value)



# keys mathod
# user_info_keys=user_info.keys()
# print(user_info_keys)



# # item method
# user_item=user_info.items()
# print(user_info)
# print(type(user_item))

for key , value in user_info.items():
    print(f"key is {key} and value is {value}")