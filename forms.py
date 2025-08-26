from django import forms

class ContactForm(forms.Form):
    name = forms.Charfield(max_length=100, label="your Name")
    email = forms.EmailField(label="your Email")
    message = forms.Charfield(widget=forms.Textarea, label="Message")