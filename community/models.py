from django.db import models
from django.contrib.auth import get_user_model
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill

# Create your models here.
from django.conf import settings

class Community(models.Model):
    title = models.CharField(max_length=10)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='image/', blank=True)
    thumbnail = ProcessedImageField(upload_to='image/', blank=True,
                                processors=[ResizeToFill(100, 100)],
                                format='JPEG',
                                options={'quality': 80})
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    like_user = models.ManyToManyField(get_user_model(), related_name='like_community')

class Comment(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    community = models.ForeignKey(Community, on_delete=models.CASCADE)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='user_community')