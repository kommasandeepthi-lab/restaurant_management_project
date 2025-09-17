from django import forms
from utils.validation_utils import is_valid_email

class RegistrationForm(forms.Form):
    email = forms.EmailField()

    def clean_email(self):
        email = self.cleaned_data['email']
        if not is_valid_email(email):
            raise forms.ValidationError("Please provide a valid email address.")
        return email