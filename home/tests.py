from django.test import TestCase
from django.urls import reverse


class HomeTestClass(TestCase):
    def test_home(self):
        response = self.client.get(reverse('home:index'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/index.html')
        self.assertIn(b'<title>Holiday Homes</title>', response.content)




# def test_home():
#     client = Client()
#     response = client.get(reverse('home:index'))
#     content = response.content.decode("utf-8")
#

#     assert response.status_code == 200
#     assertTemplateUsed(response, "home/index.html")
