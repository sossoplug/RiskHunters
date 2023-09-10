from django.contrib import admin
from strategies.models import MainCategory, Strategy, Review, InvestmentPlan, SubCategory, InvestmentPlanReview, Pros, Cons, GrowthModel
from modeltranslation.admin import TranslationAdmin
from strategies.translations import ProsTranslationOptions, ConsTranslationOptions, GrowthModelTranslationOptions

# ================ ADMIN ============================
class MainCategoryAdmin(admin.ModelAdmin):
    """
    Admin view for Category
    """
    list_display    = ('name', 'description', 'created', 'updated')
    search_fields   = ('name',)
    list_filter     = ('created', 'updated')


class SubCategoryAdmin(admin.ModelAdmin):
    """
    Admin view for Category
    """
    list_display    = ('name', 'main_category', 'description', 'created', 'updated')
    search_fields   = ('name', 'main_category__name',)
    list_filter     = ('created', 'updated', 'main_category')



class StrategyAdmin(admin.ModelAdmin):
    """
    Admin view for Strategy
    """
    list_display    = ('name', 'user', 'ranking', 'created', 'updated')
    search_fields   = ('name', 'user__username',)
    list_filter     = ('created', 'updated', 'ranking_terminated')


class ReviewAdmin(admin.ModelAdmin):
    """
    Admin view for Review
    """
    list_display    = ('user', 'strategy', 'rating', 'created', 'updated')
    search_fields   = ('user__username', 'strategy__name',)
    list_filter     = ('created', 'updated', 'rating')


class InvestmentPlanAdmin(admin.ModelAdmin):
    """
    Admin view for InvestmentPlan
    """
    list_display    = ('name', 'user', 'category', 'initial_capital', 'risk', 'reward', 'created', 'updated')
    search_fields   = ('name', 'user__username', 'category__name',)
    list_filter     = ('created', 'updated', 'public', 'strategy_type')


class InvestmentPlanReviewAdmin(admin.ModelAdmin):
    """
        Admin view for InvestmentPlanReviewAdmin
    """
    list_display    = ('user', 'investment_plan', 'rating', 'created', 'updated')
    search_fields   = ('user__username', 'investment_plan__name',)
    list_filter     = ('created', 'updated', 'rating')


# ================ PROS ADMIN ============================
class ProsAdmin(TranslationAdmin):
    """
    Admin view for Pros
    """
    list_display    = ('name', 'description', 'created', 'updated')
    search_fields   = ('name', )
    list_filter     = ('created', 'updated')


# ================ CONS ADMIN ============================
class ConsAdmin(TranslationAdmin):
    """
    Admin view for Cons
    """
    list_display    = ('name', 'description', 'created', 'updated')
    search_fields   = ('name', )
    list_filter     = ('created', 'updated')


# ================ GROWTH MODEL ADMIN ============================
class GrowthModelAdmin(TranslationAdmin):
    """
    Admin view for GrowthModel
    """
    list_display    = ('name', 'description', 'created', 'updated')
    search_fields   = ('name', )
    list_filter     = ('created', 'updated', 'calculable')
    filter_horizontal = ('pros', 'cons')



# Register your models here.
admin.site.register(MainCategory, MainCategoryAdmin)
admin.site.register(SubCategory, SubCategoryAdmin)
admin.site.register(Strategy, StrategyAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(InvestmentPlan, InvestmentPlanAdmin)
admin.site.register(InvestmentPlanReview, InvestmentPlanReviewAdmin)
admin.site.register(Pros, ProsAdmin)
admin.site.register(Cons, ConsAdmin)
admin.site.register(GrowthModel, GrowthModelAdmin)
# =========================================================
