from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
	
    class Meta(object):
        db_table = u'users'
        app_label = 'blog'
        verbose_name = u'Пользователь'
        verbose_name_plural = u'Пользователи'
