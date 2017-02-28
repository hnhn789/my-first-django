from django import forms
from django.forms.extras.widgets import SelectDateWidget

import account.forms

class SignupForm(account.forms.SignupForm):
    real_name = forms.CharField(max_length=100);