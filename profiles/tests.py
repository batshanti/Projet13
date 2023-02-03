from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from profiles.models import Profile


class ProfileTestClass(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username="user_test",
            password="passwordtest1234",
            email="user_test@yahoo.com"
        )
        self.profile = Profile.objects.create(user=self.user, favorite_city="test_city")

    def test_profile_index(self):
        response = self.client.get(reverse('profiles:index'))
        self.assertIn(b'<title>Profiles</title>', response.content)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/index.html')

    def test_profile_detail(self):
        response = self.client.get(reverse('profiles:profile', args=[self.user.username]))
        self.assertIn(b'<title>user_test</title>', response.content)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/profile.html')
