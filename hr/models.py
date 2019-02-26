from django.db import models
from django.utils import timezone
# Create your models here.



class JobCategory(models.Model):
	category = models.CharField('category', max_length=200 )


	def __str__(self):
		return self.category


class Job(models.Model):
	job_title = models.CharField(max_length=200)
	job_image = models.FileField(upload_to='uploads/')
	job_description = models.TextField()
	job_keywords = models.CharField(max_length=400, null=True)
	job_location = models.CharField(max_length=400, null=True)
	job_category = models.ForeignKey(JobCategory, on_delete="models.CASCADE", null =True)
	job_duties = models.TextField()
	job_qualifications = models.TextField()
	published_date = models.DateTimeField(default=timezone.now())

	

	def __str__(self):
		return self.job_title