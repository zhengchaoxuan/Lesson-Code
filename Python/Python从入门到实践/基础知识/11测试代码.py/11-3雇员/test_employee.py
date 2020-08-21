# 该代码是python从入门到实践的练习源码
# date ：2020/07/21
# version : 0.1

import unittest
from employee import Employee

class TextEmloyee(unittest.TestCase):
    def setUp(self):
        self.employee1 = Employee('zheng','chaoxuan',3000)
        self.employee2 = Employee('zheng','chaoxuan',3000)
        self.employee2.give_raise(2000)
    
    def test_give_default_raise(self):
        self.assertEqual(self.employee1.salary,3000)
    
    def test_give_custom_raise(self):
        self.assertEqual(self.employee2.salary,5000)

unittest.main()