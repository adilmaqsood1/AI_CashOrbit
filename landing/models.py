from django.db import models

class PricingPlan(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    billing_cycle = models.CharField(max_length=50, choices=[
        ('monthly', 'Monthly'),
        ('quarterly', 'Quarterly'),
        ('annually', 'Annually'),
    ], default='monthly')
    is_popular = models.BooleanField(default=False)
    description = models.TextField()
    
    def __str__(self):
        return f"{self.name} - {self.price}/{self.get_billing_cycle_display()}"

class PlanFeature(models.Model):
    plan = models.ForeignKey(PricingPlan, related_name='features', on_delete=models.CASCADE)
    feature = models.CharField(max_length=200)
    is_included = models.BooleanField(default=True)
    
    def __str__(self):
        return f"{self.feature} - {self.plan.name}"