from django.conf import settings
from django.urls import path, include
from django.views.generic.base import TemplateView # new

urlpatterns = [
    path('accounts/profile/', TemplateView.as_view(template_name='home.html'), name='home'), # new
    
]