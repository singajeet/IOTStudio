from django.conf.urls import url
from . import views
from django.views.generic.base import TemplateView


urlpatterns = [
        url('', views.index, name="index"),
        url(r'^$', TemplateView.as_view(template_name='test.html'), name='test'),
]
