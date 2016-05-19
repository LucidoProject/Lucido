from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'infographics', views.infographics, name='infographics'),
	url(r'^$', views.opendata, name='opendata'),
]
