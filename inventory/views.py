from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class InventoryView(LoginRequiredMixin, TemplateView):
    template_name = 'inventory/inventory.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Add inventory data to context here when models are implemented
        return context
