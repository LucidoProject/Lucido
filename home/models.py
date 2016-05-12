from django.db import models
from django.utils import timezone

class OpenData(models.Model):
	''' Tabella che rappresenta uno sheet opendata.
	'''

	title = models.CharField(max_length=200)
	description = models.TextField()
	sheet = models.FileField()
	upload_date = models.DateTimeField(default=timezone.now)
	publish_date= models.DateTimeField(blank=True, null=True)

	def __str__(self):
		return self.title


