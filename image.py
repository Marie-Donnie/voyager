#!/usr/bin/env python

import random
import string
import os




def create_image(name):
    flavor_uuid = ''.join([random.choice(string.ascii_letters
                        + string.digits) for n in range(8)])
    path = "images/" + flavor_uuid
    f = open(path,"w+")
    f.write(name)
    f.close()
    return flavor_uuid

def get_image(flavor_uuid):
    path = "images/" + flavor_uuid
    try:
        with open(path) as f:
            name = f.readlines()
            return name
    except IOError:
        print("Image not accessible")
