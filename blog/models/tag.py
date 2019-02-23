from django import models


class Tag(models.Model):
    name = models.CharField(max_length=256)

    class Meta:
        db_table = u'tags'
        app_label = 'blog'
