#!/usr/bin/env python

"""Emulate an oversimplified model of OpenStack

Usage:
    voyager [-h | --help] [-v | --version] <module> [<args>...]

Options:
    -h --help      Show this help
    -v --version   Show version number

Module:
    compute      The compute module
    image        The image module

"""


from docopt import docopt
from utils import (doc, doc_lookup)

import compute as cpt
import image as img
import identity as ide


def create_image(name):
    print(img.create_image(name))

def create_user():
    print(ide.create_user())

def create_vm_from_image(token, image):
    if ide.validate_token(token):
        print(img.get_image(image))




if __name__ == '__main__':
    create_vm_from_image(42, "mhosyGKW")
    # args = docopt(__doc__,
    #               version='voyager version 1.0.0',
    #               options_first=True)
    # argv = [args['<module>']] + args['<args>']
    # doc_lookup(args['<module>'], args)
