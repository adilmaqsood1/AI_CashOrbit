from django.shortcuts import render

# Create your views here.

def expenses(request):
    return render(request, 'expenses/expenses.html')
