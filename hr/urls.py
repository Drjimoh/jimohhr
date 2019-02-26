from django.urls import path
from . import views

app_name = 'hr'

urlpatterns = [
	path('results/', views.JobSearchView.as_view(), name='results'),
	path('', views.HomePageView.as_view(), name='index'),

]