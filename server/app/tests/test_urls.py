from django.test import TestCase
from django.urls import reverse, resolve

class TestUrls(TestCase):

	def test_urls(self):
		self.assertEqual(resolve(reverse('search')).view_name, 'search')