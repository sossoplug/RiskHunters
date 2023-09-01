# users/forms.py

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext_lazy as _

class UserRegisterForm(UserCreationForm):
    """
    Form for registering a new user.

    Attributes:
        email (EmailField): The email field of the form.
    """
    email       = forms.EmailField()

    class Meta:
        model   = User
        fields  = ['username', 'email', 'password1', 'password2']
        labels  = {
            'username':     _('Username'),
            'email':        _('Email'),
            'password1':    _('Password'),
            'password2':    _('Confirm Password'),
        }

    def clean(self):
        """
        Validates the form data.

        Raises:
            ValidationError: If the username or email is already taken, or if the passwords do not match.

        Returns:
            dict: The cleaned data of the form.
        """
        try:
            cleaned_data  = super().clean()
            username      = cleaned_data.get('username')
            email         = cleaned_data.get('email')
            password1     = cleaned_data.get('password1')
            password2     = cleaned_data.get('password2')

            if User.objects.filter(username=username).exists():
                raise forms.ValidationError(_('Username is already taken.'))

            if User.objects.filter(email=email).exists():
                raise forms.ValidationError(_('Email is already taken.'))

            if password1 != password2:
                raise forms.ValidationError(_('Passwords do not match.'))

            return cleaned_data

        except forms.ValidationError as e:
            raise forms.ValidationError(_('An error occurred. Please try again.'))
