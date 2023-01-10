from django.urls import reverse
from django.test import Client
from pytest_django.asserts import assertTemplateUsed


def test_home():
    client = Client()
    response = client.get(reverse('home:index'))
    content = response.content.decode("utf-8")

    assert "<title>Holiday Homes</title>" in content
    assert response.status_code == 200
    assertTemplateUsed(response, "home/index.html")
