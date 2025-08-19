from django import forms
from .models import Feedback

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['name', 'feedback_text']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Name'}),
            'feedback_text': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Write your feedback here...'}),
        }

class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'placeholder': 'Enter your full name'})
    )
    email = forms.EmailFiels(
        widget=forms.EmailInput(attrs={'placeholder': 'Enter your email address'})
    )
    message = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder': 'Write your message here...', 'rows': 5})
    )