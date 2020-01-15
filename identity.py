#!/usr/bin/env python


import random
import string



def create_user():
    user = ''.join([random.choice(string.ascii_letters
            + string.digits) for n in range(18)])
    return user

def validate_token(token):
    return True
