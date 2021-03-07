import unittest
import time

class TestCase1(unittest.TestCase):
    # def setUp(self):
    # def tearDown(self):
    name = '魏桐辉'
    def setUp(self):
        print('set_up')
    def tearDown(self):
        print('tear_down')
    def testCase1(self):
        time.sleep(1)
        print('aaa')

    def testCase2(self):
        print('bbb')
        time.sleep(1)


class TestCase2(unittest.TestCase):
    # def setUp(self):
    # def tearDown(self):
    def testCase1(self):
        print('aaa1')
        time.sleep(1)

    def testCase2(self):
        print('bbb1')
        time.sleep(1)
        self.assertEqual('a','v')
'''
把测试发现的用例全部读到li里
'''
li = []
def handler(obj):
    if hasattr(obj, '_tests'):
        for i_obj in obj._tests:
            handler(i_obj)
    else:
        li.append(obj)


if __name__ == "__main__":
    # 此用法可以同时测试多个类
    suite1 = unittest.TestLoader().loadTestsFromTestCase(TestCase1)
    suite2 = unittest.TestLoader().loadTestsFromTestCase(TestCase2)
    t = unittest.TestLoader().discover('.')
    # print(t)
    # print(hasattr(t, '_tests'))
    # print(t._tests)
    # print(hasattr(t._tests[0]._tests[0]._tests[0], '_tests'))
    li = []
    handler(t)
    for i in li:
        print(dir(i))
    # print(t._tests[0]._tests[0]._tests[0].name)
    # print(t._tests[0]._tests[0]._tests[0])
    # suite = unittest.TestSuite([suite1, suite2])
    # print(suite)
    # res = unittest.TextTestRunner(verbosity=2).run(t)
    # print(res)
    # print('All case number')
    # print(res.testsRun)
    # print('Failed case number')
    # print(len(res.failures))
    # print('Failed case and reason')
    # print(res.failures)
    # for case, reason in res.failures:
    #     print(type(case.id()))
    #     print(type(reason))
#
# from celerysaa import celeryWorker
# if __name__ == "__main__":
#     # 此用法可以同时测试多个类
#
#     t = unittest.TestLoader().discover('.')
#     tests = t._tests
#     li = []
#     li.append(t._tests[0]._tests[0]._tests[0])
#     li.append(t._tests[0]._tests[0]._tests[1])
#     li.append(t._tests[0]._tests[1]._tests[0])
#     li.append(t._tests[0]._tests[1]._tests[1])
#     print(li)
#     # res = unittest.TextTestRunner(verbosity=2).run(t._tests[0]._tests[0]._tests[0])
#     for i in li:
#         celeryWorker.delay(i)

def get_task():
    t = unittest.TestLoader().discover('.')
    tests = t._tests
    li = []
    li.append(t._tests[0]._tests[0]._tests[0].__str__())
    li.append(t._tests[0]._tests[0]._tests[1].__str__())
    li.append(t._tests[0]._tests[1]._tests[0].__str__())
    li.append(t._tests[0]._tests[1]._tests[1].__str__())
    return li