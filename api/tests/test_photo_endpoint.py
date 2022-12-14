import json
from urllib.parse import urljoin

from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient

from api.tests.factories import PhotoFactory
from photo.models import Photo


class TestPhotoEndpoint(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.test_server = "http://testserver"
        self.user = User.objects.create_user(
            username="admin", email="user1@test.com", is_staff=True
        )
        self.user.set_password("password1")
        self.user.save()

    def test_photo_list(self):
        self.client.force_authenticate(self.user)
        photo_1 = PhotoFactory(user=self.user)
        photo_2 = PhotoFactory(user=self.user)
        response = self.client.get(reverse("photo-list"))
        received_data = json.loads(response.content)
        expected_data = [
            {
                "id": photo_1.pk,
                "image": urljoin(self.test_server, photo_1.image.url),
            },
            {
                "id": photo_2.pk,
                "image": urljoin(self.test_server, photo_2.image.url),
            },
        ]

        assert response.status_code == 200
        assert received_data == expected_data

    def test_photo_detail(self):
        self.client.force_authenticate(self.user)
        photo = PhotoFactory(user=self.user)
        response = self.client.get(
            reverse("photo-detail", kwargs={"pk": photo.pk})
        )
        received_data = json.loads(response.content)
        expected_data = {
            "id": photo.pk,
            "location": photo.location,
            "date": photo.date.strftime("%Y-%m-%d"),
            "description": photo.description,
            "people": photo.people,
            "image": urljoin(self.test_server, photo.image.url),
        }
        assert response.status_code == 200
        assert received_data == expected_data
