from django.shortcuts import render

# Create your views here.

def banking(request):
    return render(request, 'banking/banking.html')
