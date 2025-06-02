from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views import View

# Create your views here.
@method_decorator(login_required, name='dispatch')
class AIInsightsView(View):
    def get(self, request):
        context = {
            'page_title': 'AI Insights',
        }
        return render(request, 'ai_insights/ai_insights.html', context)
