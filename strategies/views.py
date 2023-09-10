from django.shortcuts import render
from django.http import JsonResponse
from django.utils.translation import gettext_lazy as _
from .models import InvestmentPlan, GrowthModel
from .forms import InvestmentPlanCalculationForm, SaveInvestmentPlanForm

# Create your views here.

def create_investment_plan(request):
    """
    View to handle the creation and calculation of an investment plan, following the GCC.

    Args:
        request (HttpRequest): The HTTP request instance.

    Returns:
        JsonResponse: The HTTP response as JSON.
    """
    try:
        if request.method == 'POST':
            form = InvestmentPlanCalculationForm(request.POST)
            if form.is_valid():
                # ... (Perform necessary calculations)
                # Assume some pseudo calculations here. Please replace with the actual formulae.

                investplan                                                          = form.instance
                investplan.expected_growth_percent , investplan.growth_in_cash, investplan.amount_risked_per_position      = investplan.calculate_linear_expected_growth()

                investplan.potential_cash_loss                                      = investplan.calculate_potential_loss()
                investplan.potential_net_profit                                     = investplan.calculate_net_profit()
                investplan.profit_factor                                            = investplan.calculate_profit_factor()


                # investplan.save(commit=False)
                # print(investplan)

                response_data = {
                    'success': True,
                    'message': _('Calculation successful'),
                    'amount_risked_per_position':   investplan.amount_risked_per_position,
                    'expected_growth_percent':      investplan.expected_growth_percent,
                    'growth_in_cash':               investplan.growth_in_cash,
                    'potential_cash_loss':          investplan.potential_cash_loss,
                    'potential_net_profit':         investplan.potential_net_profit,
                    'profit_factor':                investplan.profit_factor,
                    'strategy_type':                investplan.strategy_type
                }
                return JsonResponse(response_data)
            else:
                response_data = {'success': False, 'message': _('Form is not valid')}
                return JsonResponse(response_data)
        else:
            form                                    = InvestmentPlanCalculationForm()
            models                                  = GrowthModel.objects.all().order_by('-calculable')
            context                                 =  {'form': form,
                                                        'title': _('Investment Plan Estimation'),
                                                        'models': models}
            return render(request, 'strategies/calculate_investment_plan.html', context )

    except Exception as e:
        response_data = {'success': False, 'message': str(e)}
        return JsonResponse(response_data)


def save_investment_plan(request):
    """
    View to handle the saving of an investment plan, following the GCC.

    Args:
        request (HttpRequest): The HTTP request instance.

    Returns:
        JsonResponse: The HTTP response as JSON.
    """
    try:
        if request.method == 'POST':
            form = SaveInvestmentPlanForm(request.POST)
            if form.is_valid():
                form.save()
                response_data = {'success': True, 'message': _('Investment Plan saved successfully')}
                return JsonResponse(response_data)
            else:
                response_data = {'success': False, 'message': _('Form is not valid')}
                return JsonResponse(response_data)
        else:
            response_data = {'success': False, 'message': _('Invalid request method')}
            return JsonResponse(response_data)
    except Exception as e:
        response_data = {'success': False, 'message': str(e)}
        return JsonResponse(response_data)
