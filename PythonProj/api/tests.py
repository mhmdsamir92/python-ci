from django.test import TestCase
from .utils import math
import mock

class TestMath(TestCase):
    
    def test_sum(self):
        res = math.add(1, 2)
        self.assertEqual(res, 3)

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

    def test_add_api(self):
        response = self.client.get(
            path='/api/add?num1=5&num2=7',
            content_type='application/json'
        )
        self.assertEqual(response.json(), {
            "result": 12
        })


