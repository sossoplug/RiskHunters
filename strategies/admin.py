from django.contrib import admin
from .models import Category, Strategy, Review, InvestmentPlan

# ================ ADMIN ============================
class CategoryAdmin(admin.ModelAdmin):
    """
    Admin view for Category
    """
    list_display    = ('name', 'description')
    search_fields   = ['name', 'description']

class StrategyAdmin(admin.ModelAdmin):
    """
    Admin view for Strategy
    """
    list_display    = ('name', 'description', 'ranking_terminated', 'ranking')
    list_filter     = ('ranking_terminated', 'ranking')
    search_fields   = ['name', 'description']

class ReviewAdmin(admin.ModelAdmin):
    """
    Admin view for Review
    """
    list_display    = ('user', 'strategy', 'rating', 'review')
    list_filter     = ('rating',)
    search_fields   = ['review']

class InvestmentPlanAdmin(admin.ModelAdmin):
    """
    Admin view for InvestmentPlan
    """
    list_display    = ('user', 'name', 'category', 'initial_capital', 'risk', 'reward', 'risk_percent_per_position', 'numbers_of_position', 'win_rate_ratio', 'strategy_type', 'expected_growth_percent', 'growth_in_cash')
    list_filter     = ('category', 'strategy_type')
    search_fields   = ['name']

# Register your models here.
admin.site.register(Category, CategoryAdmin)
admin.site.register(Strategy, StrategyAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(InvestmentPlan, InvestmentPlanAdmin)
# =========================================================
