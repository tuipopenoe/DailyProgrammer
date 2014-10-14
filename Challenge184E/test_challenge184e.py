#!python2
# Tui Popenoe
# test_challenge184e.py - Smart Stack List

from Challenge184E import *
import sys
from StringIO import StringIO

def test_init():
    """Test the init method on the smart stack list class."""
    smart_stack_list = SmartStackList()
    assert(isinstance(smart_stack_list.sorted_list, list))
    assert(isinstance(smart_stack_list.stack_list))

def test_push():
    """Test the push method on the smart stack list class."""
    smart_stack_list = SmartStackList()
    for i in range(10):
        smart_stack_list.push(i)

    assertEqual([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], smart_stack_list.sorted_list)
    assertEqual([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], smart_stack_list.stack_list)

def test_pop():
    """Test the pop method on the smart stack list class."""
    smart_stack_list = SmartStackList()
    for i in range(10):
        smart_stack_list.push(i)
    for i in range(5):
        smart_stack_list.pop()
    assertEqual([0, 1, 2, 3, 4], smart_stack_list.sorted_list)
    assertEqual([0, 1, 2, 3, 4], smart_stack_list.stack_list)

def test_size():
    """Test the size method on the smart stack list class."""
    smart_stack_list = SmartStackList()
    assertEqual(smart_stack_list.size(), 0)
    for i in range(10):
        smart_stack_list.push(i)
    assertEqual(smart_stack_list.size(), 10)

def test_remove_greater():
    """Test the remove greater method on the smart stack list class."""
    smart_stack_list = SmartStackList()
    for i in range(10):
        smart_stack_list.push(i)
    smart_stack_list.remove_greater(4)
    assertEqual([0, 1, 2, 3, 4], smart_stack_list.sorted_list)
    assertEqual([0, 1, 2, 3, 4], smart_stack_list.stack_list)

def test_display_stack():
    """Test the display stack method on the smart stack list class."""
    smart_stack_list = SmartStackList()
    for i in range(10):
        smart_stack_list.push(i)
    saved_stdout = sys.stdout
    try:
        out = StringIO()
        sys.stdout = out
        smart_stack_list.display_stack()
        output = out.getvalue().strip()
        assert(output == '[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]')
    finally:
        sys.stdout = saved_stdout

def test_display_ordered():
    """Test the display ordered method on the smart stack list class."""
        smart_stack_list = SmartStackList()
    for i in range(10):
        smart_stack_list.push(i)
    saved_stdout = sys.stdout
    try:
        out = StringIO()
        sys.stdout = out
        smart_stack_list.display_ordered()
        output = out.getvalue().strip()
        assert(output == '[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]')
    finally:
        sys.stdout = saved_stdout