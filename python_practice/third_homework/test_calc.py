from curses.ascii import isdigit

import pytest

from python_practice.third_homework.calculator import Calculator




class Test_Talc:
    def setup_class(self):
        print("这是一个类级别的：开始计算")
    def teardown(self):
        print("这是一个类级别的：结束计算")
    def setup(self):
        print("开始计算")
        self.calc=Calculator()

    def teardown(self):
        print("结束计算")

    @pytest.mark.parametrize('a,b,expect',[(1,2,3),(0,0,0),('a','b','c'),(100,200,300),(-1,-2,-3),(0.1,0.2,0.3),('一','二','三')])
    def test_add(self,a,b,expect):
            print("测试相加")
            result=self.calc.add(a,b)
            assert expect == result

    @pytest.mark.parametrize('a,b,expect',[(0.1,0.2,0.3),(3.1415,3.44,2),(100.001,100.002,200)])
    def test_float(self,a,b,expect):
        print("浮点数相加")
        result=round(self.calc.add(a,b),2)
        assert  expect == result
    @pytest.mark.parametrize('a,b,expect',[(2,1,2),(6,3,2),(1.3,2,3),(1,0,3),(-1,-2,0.5),(0.2,0.05,4),(0,1,0)])
    def test_div(self,a,b,expect):
         if b == 0:
            raise("被除数不能为0")

         else:
            print("测试相除")
            result=self.calc.div(a,b)
            assert expect == result




