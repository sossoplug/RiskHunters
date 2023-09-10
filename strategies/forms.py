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

        widgets = {
            'initial_capital': forms.NumberInput(attrs={'class': 'form-control', 'style': 'width:200px'}),
            'risk': forms.NumberInput(attrs={'class': 'form-control', 'style': 'width:200px'}),
            'reward': forms.NumberInput(attrs={'class': 'form-control', 'style': 'width:200px'}),
            'risk_percent_per_position': forms.NumberInput(attrs={'class': 'form-control', 'style': 'width:200px'}),
            'numbers_of_position': forms.NumberInput(attrs={'class': 'form-control', 'style': 'width:200px'}),
            'win_rate_ratio': forms.NumberInput(attrs={'class': 'form-control', 'style': 'width:200px'}),
            'strategy_type': forms.Select(attrs={'class': 'form-control', 'style': 'width:200px'}),
        }



class SaveInvestmentPlanForm(forms.ModelForm):
    class Meta:
        model   = InvestmentPlan
        fields  = [
            'name',
            'category',
            'public'
        ]
