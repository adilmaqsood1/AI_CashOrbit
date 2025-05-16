from django.urls import path
from . import views

urlpatterns = [
    path('', views.LandingPageView.as_view(), name='landing'),
    path('features/', views.FeaturesPageView.as_view(), name='features'),
    path('features/advanced-user-rights/', views.FeatureAdvancedUserRightsView.as_view(), name='feature_advanced_user_rights'),
    path('features/assembly/', views.FeatureAssemblyView.as_view(), name='feature_assembly'),
    path('features/batch-expiry/', views.FeatureBatchExpiryView.as_view(), name='feature_batch_expiry'),
    path('features/backups-security/', views.FeatureBackupsSecurityView.as_view(), name='feature_backups_security'),
    path('features/business-analysis/', views.FeatureBusinessAnalysisView.as_view(), name='feature_business_analysis'),
    path('features/cloud/', views.FeatureCloudView.as_view(), name='feature_cloud'),
    path('features/easy-setup/', views.FeatureEasySetupView.as_view(), name='feature_easy_setup'),
    path('features/tax/', views.FeatureTaxView.as_view(), name='feature_tax'),
    path('features/inventory/', views.FeatureInventoryView.as_view(), name='feature_inventory'),
    path('features/multi-currency/', views.FeatureMultiCurrencyView.as_view(), name='feature_multi_currency'),
    path('features/purchases/', views.FeaturePurchasesView.as_view(), name='feature_purchases'),
    path('features/sales/', views.FeatureSalesView.as_view(), name='feature_sales'),
    path('feature_ai_insights/', views.FeatureAIInsightsView.as_view(), name='feature_ai_insights')
]