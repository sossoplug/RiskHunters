# home/views.py

from django.shortcuts import render
from django.utils.translation import gettext_lazy as _
from core.helper import set_user_language

def home(request):
    set_user_language(request)
    context = {
        'title': _('Riskhunters'),
    }
    return render(request, 'home/base.html', context)
