# making a password generator

import random


def passwordg(lenpass):
    chars = "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
    password = ""
    for i in range(lenpass):
        password += random.choice(chars)
    return password
