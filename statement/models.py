from django.db import models

# Create your models here.
class xyz(models.Model):
	credit=models.CharField(max_length=100,blank=True)
	debit=models.CharField(max_length=100,blank=True)
	name=models.CharField(max_length=100,blank=True)
	date=models.DateField(blank=True)

	def __str__(self):
		return self.name




