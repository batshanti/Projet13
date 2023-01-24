from django.test import TestCase
from django.urls import reverse
from lettings.models import Address, Letting


class LettingTestClass(TestCase):
    def setUp(self):
        self.address = Address.objects.create(
            number=1,
            street="street test",
            city="TestCity",
            state="testing",
            zip_code=11111,
            country_iso_code="TEST"
        )
        self.letting = Letting.objects.create(title="Test Letting", address=self.address)

    def test_lettings_index(self):
        response = self.client.get(reverse('lettings:index'))
        self.assertIn(b'<title>Lettings</title>', response.content)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'lettings/index.html')

    def test_lettings_detail(self):
        response = self.client.get(reverse('lettings:letting', args=[self.letting.id]))
        self.assertEquals(response.status_code, 200)
        self.assertIn(b'<title>Test Letting</title>', response.content)
        self.assertTemplateUsed(response, 'lettings/letting.html')
