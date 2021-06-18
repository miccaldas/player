#!/usr/bin/env python3

""" Script to automate the push process in Git """
from colr import color
from sultan.api import Sultan


def push():
    """ User will define a title for the commit and Sultan will add, commit and push """

    title = input(color('What is the title of the commit?', fore='#feb729'))

    with Sultan.load() as s:
        s.git('add .').run()
        s.git('commit -m ' + title).run()
        s.git('push origin main').run()
        s.git('push origin_gogs main').run()


if __name__ == '__main__':
    push()
