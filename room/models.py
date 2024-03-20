from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
# Create your models here.

class Room(models.Model):
    name = models.CharField(max_length=255)
    # slug = models.SlugField(unique=True)
    slug = models.SlugField(unique=True,max_length=255)
    def save(self, **kwargs):
        self.slug = slugify(self.name)
        super(Room, self).save(**kwargs)

class Message(models.Model):
    room = models.ForeignKey(Room, related_name='messages', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='messages', on_delete=models.CASCADE)
    content = models.TextField(null=True, blank=True)
    file_data = models.TextField(null=True, blank=True)
    file_name = models.TextField(null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('date_added',)