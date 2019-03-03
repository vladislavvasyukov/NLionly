from django.db import models
from django.contrib.contenttypes.fields import GenericRelation


class Comment(models.Model):
    article = models.ForeignKey('Article', related_name='comments', on_delete=models.PROTECT)
    user = models.ForeignKey('User', related_name='comments', on_delete=models.PROTECT)
    pub_date = models.DateTimeField(auto_now_add=True)
    text = models.TextField(default='')
    votes = GenericRelation('LikeDislike', related_query_name='comments')
    
    class Meta:
        db_table = u'comments'
        app_label = 'blog'
        verbose_name = u'Комментарий'
        verbose_name_plural = u'Комментарии'
