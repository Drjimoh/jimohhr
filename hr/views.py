from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.views import generic, View
from .models import *
from .forms import *

# Create your views here.

class HomePageView(generic.ListView):
	model = JobCategory
	template_name = 'hr/index.html'
	context_object_name = 'job'

	def get_queryset(self): 
		return JobCategory.objects.all()



'''class MyFormView(View):
	form_class = MyForm
	initial = {'key':'value'}
	template_name = 'hr/results.html'

	def get(self, request, *args, **kwargs):
		form = self.form_class(initial=self.initial)
		return render(request, self.template_name, {'form':form})
'''
	





class JobSearchView(generic.ListView):
	model = Job
	template_name = 'hr/results.html'
	context_object_name = 'job_results'

	def get_queryset(request): 
		return Job.objects.filter(job_keywords=request.POST['keywords'], job_location=request.POST['location'], job_category=request.POST['item'])

