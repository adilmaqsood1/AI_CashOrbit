from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, UpdateView, DetailView, TemplateView
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.contrib import messages

# Forms will be defined in forms.py
from .forms import UserRegistrationForm, UserLoginForm, UserProfileForm

# Service layer for business logic
from .services import user_service


class LoginView(TemplateView):
    template_name = 'users/login.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = UserLoginForm()
        return context
    
    def post(self, request, *args, **kwargs):
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Login successful!')
                return redirect('dashboard')
            else:
                messages.error(request, 'Invalid username or password')
        return render(request, self.template_name, {'form': form})


class RegisterView(CreateView):
    model = User
    form_class = UserRegistrationForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('login')
    
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Registration successful! Please log in.')
        return response


class ProfileView(LoginRequiredMixin, DetailView):
    model = User
    template_name = 'users/profile.html'
    context_object_name = 'user_profile'
    
    def get_object(self):
        return self.request.user


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserProfileForm
    template_name = 'users/profile_update.html'
    success_url = reverse_lazy('profile')
    
    def get_object(self):
        return self.request.user
    
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Profile updated successfully!')
        return response


def logout_view(request):
    logout(request)
    messages.info(request, 'You have been logged out.')
    return redirect('login')


class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'users/dashboard.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Get user-specific dashboard data from service layer
        context['dashboard_data'] = user_service.get_dashboard_data(self.request.user)
        return context


class SalesView(LoginRequiredMixin, TemplateView):
    template_name = 'users/sales.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # In a real application, you would get sales data from a service layer
        # For now, we'll just return an empty context
        return context


class SettingsView(LoginRequiredMixin, TemplateView):
    template_name = 'users/settings.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # You could add additional settings-related context here if needed
        return context


class ReportsView(LoginRequiredMixin, TemplateView):
    template_name = 'users/reports.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Get report data from service layer
        # For now, we'll just return an empty context
        # In a real application, this would include financial report data
        return context


class PayrollView(LoginRequiredMixin, TemplateView):
    template_name = 'users/payroll.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # In a real application, you would get payroll data from a service layer
        # For now, we'll just return an empty context
        # This would include employee data, salary information, tax calculations, etc.
        return context
