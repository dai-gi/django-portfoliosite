from django.conf import settings
from django.db import models
from django.utils import timezone


class Profile(models.Model):
	title = models.CharField('タイトル', max_length=100)
	image = models.ImageField(upload_to='profile', verbose_name='イメージ画像', null=True, blank=True)
	content = models.TextField("本文")
	created = models.DateTimeField("作成日", default=timezone.now)

	def __str__(self):
		return str(self.author)
        