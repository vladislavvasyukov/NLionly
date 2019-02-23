from django import models


class User(models.Model):
	pass
	
	class Meta(object):
		db_table = u'users'
		app_label = 'blog'
		verbose_name = u'Пользователь'
		verbose_name_plural = u'Пользователи'
