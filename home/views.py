# home/views.py

from django.shortcuts import render
from django.utils.translation import gettext_lazy as _

def home(request):
    context = {
        'title': _('Riskhunters'),
    }
    return render(request, 'home/base.html', context)
