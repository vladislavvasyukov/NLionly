from django.db import models
from django.contrib.contenttypes.fields import GenericRelation


class Article(models.Model):
    author = models.ForeignKey('User', related_name='articles', verbose_name=u'Автор', on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True, verbose_name=u'Дата публикации')
    title = models.CharField(max_length=256, verbose_name=u'Заголовок')
    description = models.TextField()
    votes = GenericRelation('LikeDislike', related_query_name='articles')
    tags = models.ManyToManyField('Tag')
	
    class Meta(object):
        db_table = u'articles'
        app_label = 'blog'
        verbose_name = u'Статья'
        verbose_name_plural = u'Статьи'
