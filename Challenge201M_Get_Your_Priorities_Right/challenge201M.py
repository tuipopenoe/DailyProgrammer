#!/usr/bin/env python
# Tui Popenoe
# Challenge201M.py - Get Your Priorities Right

class DoublePriorityQueue(object):
    def __init__(self):
        self.queue = []

    def enqueue(self, string, priority_A, priority_B):
        self.queue.append({string: [priority_A, priority_B]})

    def dequeue_A(self):
        self.queue.sort(key = lambda k: k['string'][0])
        self.queue.pop()

    def dequeue_B(self):
        self.queue.sort(key = lambda k: k['string'][1])
        self.queue.pop()
    def count(self):
        return len(self.queue)

    def clear(self)
        del self.queue[:]
