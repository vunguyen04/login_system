"""
 loginSystem.py
Created by Vu Nguyen
a class that is used to create a login system with some functions:
+search: check user id and password
+create_account: create a new account with member privilege
+create_account_admin: create an admin account
"""
from cryptography import Cryptography


def create_account(in_user, in_password):
    file = open("account.txt", "a")
    if check_username(in_user) == False:
        file.write(in_user + "\n" + Cryptography(in_password).encryption() + "\n" + "member\n\n")
    else:
        print("Username exists!")
    file.close()


def create_account_admin(in_user, in_password):
    file = open("account.txt", "a")
    if check_username(in_user) == False:
        file.write(in_user + "\n" + Cryptography(in_password).encryption() + "\n" + "admin\n\n")
    else:
        print("Username exists!")
    file.close()


def check_username(in_user):
    file = open("account.txt", "r")
    readline = file.readlines()
    for i in range(0, len(readline),4):
        if in_user == readline[i].rstrip():
            return True
    return False


class LoginSystem:
    def __init__(self, in_user, in_password):
        self.username = in_user
        self.password = in_password

    def search(self):
        file = open("account.txt", "r")
        file.seek(0)
        file_readline = file.readlines()
        in_password = Cryptography(self.password).encryption()
        for i in range(0, len(file_readline), 4):
            #Use rstrip to remove \n at the end of line
            if file_readline[i].rstrip() == self.username and file_readline[i+1].rstrip() == in_password:
                self.welcome()
                file.close()
                return True

        return False

    def welcome(self):
        print("Welcome back " + self.username)

create_account("vu1","password")
create_account_admin("vu1","password")
test = LoginSystem("vu2", "quangvu")
test.search()

