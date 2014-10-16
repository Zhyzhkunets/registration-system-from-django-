from django.db import models
from django.contrib.auth.models import User, UserManager

class CustomUser(User):
    """User with app settings."""
    date_birth = models.DateField()
    phone = models.CharField(max_length=30)

    # Use UserManager to get the create_user method, etc.
    objects = UserManager()

class Post(models.Model):
    """This model for a resume"""
    title = models.CharField(max_length=50)
    body = models.TextField(max_length=10000)

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"
