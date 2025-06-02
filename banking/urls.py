from django.urls import path
from . import views

app_name = 'banking'

urlpatterns = [
    path('', views.banking, name='banking')
]