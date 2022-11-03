from django.db import models
from django.contrib.auth import get_user_model
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill

# Create your models here.
from django.conf import settings


class CustomCard(models.Model):
    supertype = models.TextField()
    types = models.TextField(null=True)
    name = models.TextField()
    image = models.TextField()
