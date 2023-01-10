from django.urls import reverse
from django.test import Client
import pytest
from pytest_django.asserts import assertTemplateUsed


client = Client()


@pytest.mark.django_db
def test_lettings_index():
    response = client.get(reverse('lettings:index'))
    content = response.content.decode("utf-8")

    assert "<title>Lettings</title>" in content
    assert response.status_code == 200
    assertTemplateUsed(response, "lettings/index.html")


@pytest.mark.django_db
def test_lettings_detail():
    url = reverse('lettings:letting', args=[2])
    response = client.get(url)
    content = response.content.decode("utf-8")

    assert response.status_code == 200
    assert "<title>Oceanview Retreat</title>" in content
