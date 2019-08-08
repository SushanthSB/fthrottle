from django.test import TestCase
from app.models import Data


class DataTest(TestCase):

	def setUp(self):
		Data.objects.create(string="hello", occurance="1234")

	def test_data_insertion(self):
		data = Data.objects.get(string="hello")
		self.assertEqual(data.string, "hello")
