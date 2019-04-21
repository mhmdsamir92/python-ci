from django.test import TestCase
from .utils import math
import mock

class TestMath(TestCase):
    
    def test_sum(self):
        res = math.add(1, 2)
        self.assertEqual(res, 3)
    
    def test_minus(self):
        res = math.minus(2, 1)
        self.assertEqual(res, 2)

class TestApi(TestCase):

    @mock.patch("api.utils.math.add", return_value=3)
    def test_add_api_exists(self, math_add_exist):
        response = self.client.get(
            path='/api/add?num1=5&num2=7',
            content_type='application/json'
        )
        math_add_exist.assert_called_once_with(5, 7)
        self.assertEqual(response.json(), {
            "result": 3
        })
    
    @mock.patch("api.utils.math.minus", return_value=2)
    def test_minus_api_exists(self, math_minus_exist):
        response = self.client.get(
            path='/api/minus?num1=7&num2=5',
            content_type='application/json'
        )
        math_minus_exist.assert_called_once_with(7, 5)
        self.assertEqual(response.json(), {
            "result": 2
        })

    def test_add_api(self):
        response = self.client.get(
            path='/api/add?num1=5&num2=7',
            content_type='application/json'
        )
        self.assertEqual(response.json(), {
            "result": 12
        })
    
    def test_minus_api(self):
        response = self.client.get(
            path='/api/minus?num1=7&num2=5',
            content_type='application/json'
        )
        self.assertEqual(response.json(), {
            "result": 2
        })


