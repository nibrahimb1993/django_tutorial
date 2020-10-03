from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from mixer.backend.django import mixer
from rest_framework import status
from rest_framework.test import APIClient


class TestUserView(TestCase):
    def test_list_users(self):
        url = reverse('list_users')
        client = APIClient()
        user = mixer.blend(User)
        user.is_staff = True
        user.save()
        client.force_authenticate(user)
        request = client.get(url)
        assert request.status_code == status.HTTP_200_OK
