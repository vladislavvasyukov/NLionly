from django import models


class Comment(models.Model):
	article = models.ForeignKey('Article', related_name='comments', on_delete=models.PROTECT)
    user = models.ForeignKey('User', related_name='comments', on_delete=models.PROTECT)
	timestamp = models.DateTimeField(auto_now_add=True)
    text = models.TextField(default='')
	
	class Meta:
        db_table = u'comments'
        app_label = 'blog'
