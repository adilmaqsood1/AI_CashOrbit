from django.urls import path
from . import views

app_name = 'ai_insights'

urlpatterns = [
    path('', views.AIInsightsView.as_view(), name='ai_insights'),
]