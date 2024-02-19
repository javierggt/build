#!/usr/bin/env python

from sys import argv
from os import environ


if 'username' in argv[1].lower():
    print(environ['GIT_USERNAME'])

if 'password' in argv[1].lower():
    print(environ['GIT_PASSWORD'])
