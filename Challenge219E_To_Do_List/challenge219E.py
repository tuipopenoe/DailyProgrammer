#!/usr/bin/env python
# Tui Popenoe
# Challenge219E.py To Do List


class ToDoList(object):
    def __init__(self):
        self.to_do_list = []

    def add_item(item):
        self.to_do_list.append(item)

    def remove_item(item):
        try:
            self.to_do_list.remove(item)
        except Exception, ex:
            pass

    def view_list():
        for item in self.to_do_list:
            print(item)

