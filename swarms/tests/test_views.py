from django.test import SimpleTestCase, TestCase
from django.urls import resolve, reverse
from unauthenticated.views import testingView
# Create your tests here.


class TestUrls(SimpleTestCase):
    """_summary_
        Testing that the home page loads, and that the view is working as expected,
        if correct template is used the correct View has been called
    """
    def test_home_url_resolves(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response, "unauthenticated/unauthenticated.html")
