from django.urls import path
from strategies.views import create_investment_plan, save_investment_plan

urlpatterns = [
    path('create_investment_plan/', create_investment_plan, name='create_investment_plan'),
    path('save_investment_plan/',   save_investment_plan,   name='save_investment_plan'),
]
