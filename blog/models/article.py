from django import models


class Article(models.Model):
	author = models.ForeignKey(User, related_name='articles', verbose_name=u'Автор')
	created = models.DateTimeField(auto_now_add=True, verbose_name=u'Дата создания')
	title = models.CharField(max_length=256, verbose_name=u'Заголовок')
    description = models.TextField()
	
    class Meta(object):
        db_table = u'articles'
        app_label = 'blog'
        verbose_name = u'Статья'
        verbose_name_plural = u'Статьи'
