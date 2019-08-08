from django.test import TestCase
from django.test import Client
from django.urls import reverse
from app.views import match, insert_position
import json
from app.models import Data

class TestUtilityFunction(TestCase):

	def test_match_if_pattern_exists(self):
		text = "preposterous"
		
		pattern_one = "pre"
		val_one = match(pattern_one, text)

		self.assertEqual(val_one[0], text)
		self.assertEqual(val_one[1], 0)

		pattern_two = "post"
		val_two = match(pattern_two, text)

		self.assertEqual(val_two[0], text)
		self.assertEqual(val_two[1], 3)

	def test_for_index_insert_position(self):
		occurance_idx = [3]

		position = insert_position(2, occurance_idx)
		self.assertEqual(position, 0)

		occurance_idx = [1, 3]
		position = insert_position(2, occurance_idx)
		self.assertEqual(position, 1)

		occurance_idx = [1, 2]
		position = insert_position(3, occurance_idx)
		self.assertEqual(position, 2)


class TestSearch(TestCase):

	def setUp(self):
		Data.objects.create(string="there", occurance="1234")
		Data.objects.create(string="other", occurance="2234")
		Data.objects.create(string="earth", occurance="3234")

	def test_empty_param(self):
		param = {
			'word': ''
		}
		path = reverse('search')
		client = Client()
		response = client.get(path, param)
		content = json.loads(response.content)
		data = []
		self.assertEqual(content["data"], data)

	def test_for_match_occurance(self):
		param = {
			'word': 'there'
		}
		path = reverse('search')
		client = Client()
		response = client.get(path, param)
		content = json.loads(response.content)
		data = ["there"]
		self.assertEqual(content["data"], data)

	def test_return_matched_words_basedon_matced_position(self):
		param = {
			'word': 'th'
		}
		path = reverse('search')
		client = Client()
		response = client.get(path, param)
		content = json.loads(response.content)
		data = ["there", "other", "earth"]
		self.assertEqual(content["data"], data)

	def test_return_pattern_not_matched(self):
		param = {
			'word': 'pre'
		}
		path = reverse('search')
		client = Client()
		response = client.get(path, param)
		content = json.loads(response.content)
		data = []
		self.assertEqual(content["data"], data)