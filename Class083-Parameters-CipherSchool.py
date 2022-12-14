def user_info(first_name,last_name,age):
    print(f"Your first name is {first_name}")
    print(f"Your last name is {last_name}")
    print(f"Your age is {age}")
user_info('Aaryan','Kashyap',18)

def user_info(first_name,last_name='unknown',age=None):
    print(f"Your first name is {first_name}")
    print(f"Your last name is {last_name}")
    print(f"Your age is {age}")
user_info('Aaryan')



