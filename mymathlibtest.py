# python -m pytest mymathlibtest.py --html=pytest-mymathlibtest.html --self-contained-html



import pytest

from mymathlib import power, factorial, fibonacci, NonIntegerException, NegativeIntegerException



class TestClass_Power:

    def test_power_1(self):

        assert power(0, 0) == 1
    
    def test_power_2(self):

        assert power(0, 1) == 0
    
    def test_power_3(self):

        assert power(1, 0) == 1
    
    def test_power_4(self):

        assert power(1, 1) == 1
    
    def test_power_5(self):

        assert power(2, 0) == 1
    
    def test_power_6(self):

        assert power(2, 1) == 2
    
    def test_power_7(self):

        assert power(2, 2) == 4
    
    def test_power_8(self):

        assert power(2, 3) == 8



class TestClass_Factorial:

    def test_factorial_1(self):

        with pytest.raises(NonIntegerException):

            factorial(3.142)
    
    def test_factorial_2(self):

        with pytest.raises(NegativeIntegerException):

            factorial(-1)
    
    def test_factorial_3(self):

        assert factorial(0) == 1
    
    def test_factorial_4(self):

        assert factorial(1) == 1
    
    def test_factorial_5(self):

        assert factorial(2) == 2
    
    def test_factorial_6(self):

        assert factorial(3) == 6



class TestClass_Fibonacci:

    def test_fibonacci_1(self):

        with pytest.raises(NonIntegerException):

            fibonacci(3.142)
    
    def test_fibonacci_2(self):

        with pytest.raises(NegativeIntegerException):

            fibonacci(-1)
    
    def test_fibonacci_3(self):

        assert fibonacci(0) == 0
    
    def test_fibonacci_4(self):

        assert fibonacci(1) == 1
    
    def test_fibonacci_5(self):

        assert fibonacci(6) == 8
    
    def test_fibonacci_6(self):

        assert fibonacci(10) == 55
    
    def test_fibonacci_7(self):

        assert fibonacci(19) == 4181
