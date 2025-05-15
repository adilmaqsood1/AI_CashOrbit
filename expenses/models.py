from django.db import models
from django.contrib.auth.models import AbstractUser

# --- User and Company ---
class Company(models.Model):
    name = models.CharField(max_length=255)
    industry = models.CharField(max_length=100)
    address = models.TextField()

class User(AbstractUser):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True, blank=True)
    role = models.CharField(max_length=50)
    
    # Add related_name to resolve clash with auth.User
    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='groups',
        blank=True,
        help_text='The groups this user belongs to.',
        related_name='expenses_user_set',
        related_query_name='expenses_user'
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name='expenses_user_set',
        related_query_name='expenses_user'
    )

# --- Clients and Employees ---
class Client(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)

class Employee(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    role = models.CharField(max_length=100)
    salary = models.DecimalField(max_digits=12, decimal_places=2)
    tax_code = models.CharField(max_length=20)

# --- Accounting Core ---
class Invoice(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    issue_date = models.DateField()
    due_date = models.DateField()
    status = models.CharField(max_length=50)
    total_amount = models.DecimalField(max_digits=12, decimal_places=2)

class Payment(models.Model):
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)
    method = models.CharField(max_length=50)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    date = models.DateField()

class Expense(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    category = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    date = models.DateField()
    project = models.ForeignKey('Project', on_delete=models.SET_NULL, null=True, blank=True)

class Report(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    type = models.CharField(max_length=100)
    generated_date = models.DateField()

# --- Banking ---
class BankAccount(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    bank_name = models.CharField(max_length=100)
    account_number = models.CharField(max_length=50)
    balance = models.DecimalField(max_digits=15, decimal_places=2)

class Reconciliation(models.Model):
    bank_account = models.ForeignKey(BankAccount, on_delete=models.CASCADE)
    date = models.DateField()
    matched_transactions = models.TextField()

# --- Inventory ---
class Product(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    sku = models.CharField(max_length=100)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)

class Warehouse(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    location = models.CharField(max_length=255)

class Stock(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

# --- Projects and Jobs ---
class Project(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    budget = models.DecimalField(max_digits=12, decimal_places=2)
    status = models.CharField(max_length=100)

class Job(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    description = models.TextField()
    allocated_cost = models.DecimalField(max_digits=12, decimal_places=2)

# --- Payroll ---
class Payroll(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    month = models.CharField(max_length=20)
    gross_pay = models.DecimalField(max_digits=12, decimal_places=2)
    net_pay = models.DecimalField(max_digits=12, decimal_places=2)
    deductions = models.DecimalField(max_digits=12, decimal_places=2)

class Payslip(models.Model):
    payroll = models.ForeignKey(Payroll, on_delete=models.CASCADE)
    generated_on = models.DateField()
    pdf_url = models.URLField()

# --- AI Insights ---
class AIInsight(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    type = models.CharField(max_length=50)  # Forecast, anomaly, etc.
    source = models.CharField(max_length=100)  # invoice, payroll, etc.
    generated_on = models.DateField()
    summary = models.TextField()


