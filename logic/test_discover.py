import unittest
import os
def get_task(dirs):
    t = unittest.TestLoader().discover(dirs)
    tests = t._tests
    li = []
    def handler(obj):
        if hasattr(obj, '_tests'):
            for i_obj in obj._tests:
                handler(i_obj)
        else:
            li.append(obj)
    handler(tests)
    return li