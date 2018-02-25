from django import forms


class UserRegistrationForm(forms.Form):
    username = forms.CharField(
        required=True,
        label='Username',
        max_length=32,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    password = forms.CharField(
        required=True,
        label='Password',
        max_length=32,
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )


class InstagramSettingsForm(forms.Form):

    tags = forms.CharField(
        required=True,
        label='Tags',
        max_length=1024,
        widget=forms.TextInput(attrs={'class': 'form-control', 'data-role': 'tags-input'})
    )

    locations = forms.CharField(
        required=False,
        label='Locations',
        max_length=1024,
        widget=forms.TextInput(attrs={'class': 'form-control', 'data-role': 'tags-input'})
    )

    likes_hour = forms.CharField(
        required=False,
        label='Likes/Hour',
        max_length=32,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    comments_hour = forms.CharField(
        required=False,
        label='Comments\Hour',
        max_length=32,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    follows_hour = forms.CharField(
        required=False,
        label='Follows\Hour',
        max_length=32,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    unfollows_hour = forms.CharField(
        required=False,
        label='Unfollows\Hour',
        max_length=32,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    posted = forms.CharField(
        required=False,
        label='Posted',
        max_length=32,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    comments = forms.CharField(
        required=False,
        label='Comments',
        max_length=32,
        widget=forms.TextInput(attrs={'class': 'form-control', 'data-role': 'tags-input'})
    )
