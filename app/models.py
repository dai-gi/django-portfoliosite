from django.conf import settings
from django.db import models
from django.utils import timezone


class Profile(models.Model):
	author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	content = models.TextField("本文")
	career = models.TextField("経歴", blank=True, null=True)
	programming_language = models.TextField("プログラミング言語", blank=True, null=True)
	created = models.DateTimeField("作成日", default=timezone.now)

	def __str__(self):
		return str(self.author)
        