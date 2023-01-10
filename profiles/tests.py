from django.urls import reverse
from django.test import Client
import pytest
from pytest_django.asserts import assertTemplateUsed

client = Client()


@pytest.mark.django_db
def test_profile_index():
    response = client.get(reverse('profiles:index'))
    content = response.content.decode("utf-8")

    assert "<title>Profiles</title>" in content
    assert response.status_code == 200
    assertTemplateUsed(response, "profiles/index.html")