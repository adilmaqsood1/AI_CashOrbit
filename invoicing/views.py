from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def invoicing(request):
    return render(request, 'invoicing/invoicing.html')

@login_required
def invoices(request):
    # In the future, this would fetch invoice data from the database
    # For now, we're just rendering the template
    return render(request, 'invoicing/invoices.html')

# Create your views here.
