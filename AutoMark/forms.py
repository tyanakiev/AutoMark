from django import forms

class UserRegistrationForm(forms.Form):
    username = forms.CharField(
        required = True,
        label = 'Username',
        max_length = 32,
        widget = forms.TextInput(attrs={'class': 'form-control'})
    )

    password = forms.CharField(
        required = True,
        label = 'Password',
        max_length = 32,
        widget = forms.PasswordInput(attrs={'class': 'form-control'})
    )