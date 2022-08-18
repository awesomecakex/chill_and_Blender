# making a password generator

import random
def passwordg(lenpass):
    chars = "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
    password = ""
    for i in range(lenpass):
        password += random.choice(chars)
    return password

def main():
    passw = passwordg(int(input("How long do you want your password to be? ")))
    print("this is your newn password - ", passw)
