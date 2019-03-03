from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from blog.managers import LikeDislikeManager


class LikeDislike(models.Model):
    LIKE = 1
    DISLIKE = -1

    VOTES = (
        (DISLIKE, 'Не нравится'),
        (LIKE, 'Нравится')
    )

    user = models.ForeignKey('User', verbose_name=u'Пользователь', on_delete=models.CASCADE)
    vote = models.SmallIntegerField(verbose_name=u"Голос", choices=VOTES)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()
 
    objects = LikeDislikeManager()

    class Meta(object):
        db_table = u'likes'
        app_label = 'blog'
