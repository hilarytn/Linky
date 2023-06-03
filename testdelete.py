#!/usr/bin/python3
""" Test delete feature
"""
from models.engine.file_storage import FileStorage
from models.user import User

fs = FileStorage()

# All States
all_users = fs.all(User)
print("All States: {}".format(len(all_users.keys())))
for user_key in all_users.keys():
    print(all_users[user_key])

new_user = User()
new_user.first_name = "Now Now"
new_user.last_name = "Dempo"
new_user.save()
all_users = fs.all(User)

print("All States: {}".format(len(all_users.keys())))
for user_key in all_users.keys():
    print(all_users[user_key])

fs.delete(new_user)
fs.save()
print("All States: {}".format(len(all_users.keys())))
for user_key in all_users.keys():
    print(all_users[user_key])
my_g = User()
my_g.save()
print("All States: {}".format(len(all_users.keys())))
for user_key in all_users.keys():
    print(all_users[user_key])
