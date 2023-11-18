from django.test import SimpleTestCase, TestCase
from unauthenticated.models import Faq


class TestModels(TestCase):
    def test_Faq_model_create(self):
        """_summary_
        When a FAQ model is created default status == shown
        """
        question = Faq.objects.create(
            summary="This is a summary", details="These are details")
        self.assertEqual(question.status, "Shown")
        question.status = "Hidden"
        self.assertEquals(question.status, "Hidden")
