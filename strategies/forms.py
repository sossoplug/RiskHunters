from django import forms
from strategies.models import InvestmentPlan

class InvestmentPlanCalculationForm(forms.ModelForm):
    class Meta:
        model   = InvestmentPlan
        fields  = [
            'initial_capital',
            'risk',
            'reward',
            'risk_percent_per_position',
            'numbers_of_position',
            'win_rate_ratio',
            'strategy_type'
        ]



class SaveInvestmentPlanForm(forms.ModelForm):
    class Meta:
        model   = InvestmentPlan
        fields  = [
            'name',
            'category',
            'public'
        ]
