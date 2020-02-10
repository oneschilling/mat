from django.forms import BooleanField
from django.utils.translation import gettext as _
from allauth.account import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Div


class CustomLoginForm(forms.LoginForm):
    """
    Custom login form that removed the labels from the form.

    """

    def __init__(self, *args, **kwargs):
        super(CustomLoginForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)

        self.fields['login'].label = False
        self.fields['password'].label = False


class CustomSignupForm(forms.SignupForm):
    """
    Custom signup form that removed the labels from the form.

    """

    def __init__(self, *args, **kwargs):
        super(CustomSignupForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)

        self.fields['email'].label = False
        self.fields['password1'].label = False
        self.fields['password2'].label = False
