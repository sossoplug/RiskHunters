# users/views.py

from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm
from django.utils.translation import gettext_lazy as _
from core.helper import set_user_language


def register(request):
    """
    View for registering a new user.

    Args:
        request (HttpRequest): The request object.

    Returns:
        HttpResponse: The response object.
    """

    set_user_language(request)

    if request.method == 'POST':
        form            = UserRegisterForm(request.POST)

        if form.is_valid():
            form.save()
            username    = form.cleaned_data.get('username')

            messages.success(request, _(f'Account created for {username}! You are now able to log in'))
            return redirect('login')
    else:
        form            = UserRegisterForm()

    return render(request, 'users/register.html', {'form': form})
