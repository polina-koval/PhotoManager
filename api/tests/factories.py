import datetime
import random

import factory
from django.contrib.auth import get_user_model
from factory.fuzzy import FuzzyDate

from photo.models import Photo

User = get_user_model()
NAMES = [
    "Liam",
    "Olivia",
    "Noah",
    "Emma",
    "Oliver",
    "Charlotte",
    "Elijah",
    "Amelia",
]


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Sequence(lambda n: "user_%d" % n)
    password = factory.Sequence(lambda n: f"password{n}")


class PhotoFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Photo

    location = factory.Sequence(lambda n: f"location{n}")
    date = FuzzyDate(start_date=datetime.date(year=1980, month=1, day=1))
    description = factory.Sequence(lambda n: f"description{n}")
    people = random.sample(NAMES, 2)
    image = factory.django.FileField(filename="image.jpg")
    user = factory.SubFactory(UserFactory)
