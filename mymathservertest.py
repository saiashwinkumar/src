# python -m pytest mymathservertest.py --html=pytest-mymathservertest.html --self-contained-html



import pytest
import requests
import json



baseUrl = 'http://localhost:5000/api/mymathserver'



class TestClass_Power:

    def test_power_1(self):

        response = requests.get(baseUrl + '/power', params={'arg1': 0, 'arg2': 0})
        assert response.status_code == 200
        assert json.loads(response.content) == {'result': 1}

    def test_power_2(self):

        response = requests.get(baseUrl + '/power', params={'arg1': 2, 'arg2': 3})
        assert response.status_code == 200
        assert json.loads(response.content) == {'result': 8}



class TestClass_Factorial:

    def test_factorial_1(self):

        response = requests.get(baseUrl + '/factorial', params={'arg1': -1})
        assert response.status_code == 400        

    def test_factorial_2(self):

        response = requests.get(baseUrl + '/factorial', params={'arg1': 3})
        assert response.status_code == 200
        assert json.loads(response.content) == {'result': 6}

    def test_factorial_3(self):

        response = requests.get(baseUrl + '/factorial', params={'arg1': 6})
        assert response.status_code == 200
        assert json.loads(response.content) == {'result': 720}



class TestClass_Fibonacci:

    def test_fibonacci_1(self):

        response = requests.get(baseUrl + '/fibonacci', params={'arg1': -1})
        assert response.status_code == 400        

    def test_fibonacci_2(self):

        response = requests.get(baseUrl + '/fibonacci', params={'arg1': 10})
        assert response.status_code == 200
        assert json.loads(response.content) == {'result': 55}

    def test_fibonacci_3(self):

        response = requests.get(baseUrl + '/fibonacci', params={'arg1': 19})
        assert response.status_code == 200
        assert json.loads(response.content) == {'result': 4181}
