from django.test import TestCase
from django.urls import reverse_lazy


class QuestionDetailViewTests(TestCase):
    def test_current_datetime(self):
        url = reverse_lazy("current_datetime")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"<body>It is now", response.content)
