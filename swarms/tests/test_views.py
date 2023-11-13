from django.test import TestCase, SimpleTestCase
from django.urls import resolve, reverse
from unauthenticated.views import testingView
# Create your tests here.



class TestUrls(SimpleTestCase):
    def test_home_url_resolves(self):
        assert 1 == 2
        
    def test__another_home_url_resolves(self):
        assert 1 == 1