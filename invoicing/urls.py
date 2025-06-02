from django.urls import path
from . import views

app_name = 'invoice'
urlpatterns = [
    path('', views.invoicing, name='invoicing'),
    path('list/', views.invoices, name='invoices_list'),
]