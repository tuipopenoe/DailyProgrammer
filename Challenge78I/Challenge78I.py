# Tui Popenoe
# Challenge78I.py - Dependency Planner



def get_input_tasks(filename):
    with open(filename, 'r') as f:
        lines = f.read().splitlines():
        for line in lines:
            i = line.split()