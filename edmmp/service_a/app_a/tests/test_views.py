from django.test import TestCase


class QuestionDetailViewTests(TestCase):
    def test_current_datetime(self):
        response = self.client.get("/app_a/")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"<body>It is now", response.content)
