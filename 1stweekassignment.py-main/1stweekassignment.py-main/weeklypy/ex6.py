user_name=input("enter your name please: ")
user_age=input("enter your age please: ")
user_age=int(user_age)
if user_age >= 10 and (user_name[0]=='a' or user_name[0]=='A'):
    print("You can watch coco")
else:
    print("You can't watch coco")