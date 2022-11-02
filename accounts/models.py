from django.contrib.auth.models import AbstractUser
from imagekit.models import ProcessedImageField
from django.db import models
from imagekit.processors import ResizeToFill

# Create your models here.


class User(AbstractUser):
    image = ProcessedImageField(
        upload_to="image/",
        blank=True,
        processors=[ResizeToFill(400, 300)],
        format="JPEG",
        options={"quality": 80},
    )
    followings = models.ManyToManyField(
        "self", symmetrical=False, related_name="followers"
    )
