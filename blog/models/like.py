from django import models


class Like(models.Model):
	user = models.ForeignKey('User', related_name='likes')
	
	class Meta(object):
		db_table = u'likes'
		app_label = 'blog'
