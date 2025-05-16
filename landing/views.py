from django.views.generic import TemplateView

class LandingPageView(TemplateView):
    template_name = 'landing/home.html'

class FeaturesPageView(TemplateView):
    template_name = 'landing/features.html'

class FeatureAdvancedUserRightsView(TemplateView):
    template_name = 'landing/feature_advanced_user_rights.html'

class FeatureAssemblyView(TemplateView):
    template_name = 'landing/feature_assembly.html'

class FeatureBatchExpiryView(TemplateView):
    template_name = 'landing/feature_batch_expiry.html'

class FeatureBackupsSecurityView(TemplateView):
    template_name = 'landing/feature_backups_security.html'

class FeatureBusinessAnalysisView(TemplateView):
    template_name = 'landing/feature_business_analysis.html'

class FeatureCloudView(TemplateView):
    template_name = 'landing/feature_cloud.html'

class FeatureEasySetupView(TemplateView):
    template_name = 'landing/feature_easy_setup.html'

class FeatureTaxView(TemplateView):
    template_name = 'landing/feature_tax.html'

class FeatureInventoryView(TemplateView):
    template_name = 'landing/feature_inventory.html'

class FeatureMultiCurrencyView(TemplateView):
    template_name = 'landing/feature_multi_currency.html'

class FeaturePurchasesView(TemplateView):
    template_name = 'landing/feature_purchases.html'

class FeatureSalesView(TemplateView):
    template_name = 'landing/feature_sales.html'
    

class FeatureAIInsightsView(TemplateView):
    template_name = 'landing/feature_ai_insights.html'