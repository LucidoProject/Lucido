from django.shortcuts import render
from .models import OpenData

def opendata(requests):
	sheets = OpenData.objects.all()
	return render(requests, 'index.html', {'sheets': sheets})
