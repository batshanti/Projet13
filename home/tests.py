from django.test import TestCase
from django.urls import reverse


class HomeTestClass(TestCase):
    def test_home(self):
        response = self.client.get(reverse('home:index'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/index.html')
        self.assertIn(b'<title>Holiday Homes</title>', response.content)
