from django.db import models

# Create your models here.

class Data(models.Model):
	string = models.CharField(max_length=128)
	occurance = models.IntegerField()

	class Meta:
		indexes = [
			models.Index(fields=['string', 'occurance',]),
		]
