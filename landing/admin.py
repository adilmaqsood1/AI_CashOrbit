from django.contrib import admin
from .models import PricingPlan, PlanFeature

class PlanFeatureInline(admin.TabularInline):
    model = PlanFeature
    extra = 3

@admin.register(PricingPlan)
class PricingPlanAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'billing_cycle', 'is_popular')
    list_filter = ('billing_cycle', 'is_popular')
    search_fields = ('name', 'description')
    inlines = [PlanFeatureInline]