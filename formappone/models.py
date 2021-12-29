from django.db import models

# Create your models here.
class StudentDetails(models.Model):
	usn=models.CharField(primary_key=True,max_length=50)
	name=models.CharField(max_length=50)
	age=models.IntegerField()
	gender=models.CharField(max_length=50)
	course=models.CharField(max_length=50)

class Meta:
	verbose_name="StudentDetails"
	verbose_name_plural="StudentDetailss"

def __str__(self):
	return self.usn