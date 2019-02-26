from django.forms import ModelForm
from .models import *

class SearchForm(ModelForm):
	class Meta:
		model = Job
		fields = ['job_keywords', 'job_location', 'job_category']