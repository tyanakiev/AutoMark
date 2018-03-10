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


class InstagramAccountForm(forms.Form):
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
        label='Tags to like',
        max_length=1024,
        widget=forms.TextInput(attrs={'class': 'form-control', 'data-role': 'tagsinput'})
    )

    likes_per_tag = forms.CharField(
        required=False,
        label='Likes per tag',
        max_length=32,
        widget=forms.TextInput(attrs={'class': 'num_of'})
    )

    percent_to_follow = forms.CharField(
        required=False,
        label='Per cent of people to follow',
        max_length=32,
        widget=forms.TextInput(attrs={'class': 'num_of'})
    )

    dont_like_tags = forms.CharField(
        required=False,
        label='Will not like if contains tag.',
        max_length=1024,
        widget=forms.TextInput(attrs={'class': 'form-control', 'data-role': 'tagsinput'})
    )

    locations = forms.CharField(
        required=False,
        label='Locations',
        max_length=1024,
        widget=forms.TextInput(attrs={'class': 'form-control', 'data-role': 'tagsinput'})
    )

    dont_like_images = forms.CharField(
        required=False,
        label='Will not like images if contains tag.',
        max_length=1024,
        widget=forms.TextInput(attrs={'class': 'form-control', 'data-role': 'tagsinput'})
    )

    comments_images = forms.CharField(
        required=False,
        label='Comments on images',
        max_length=32,
        widget=forms.TextInput(attrs={'class': 'form-control', 'data-role': 'tagsinput'})
    )

    percent_of_img_commented = forms.CharField(
        required=False,
        label='Per cent of images commented.',
        max_length=32,
        widget=forms.TextInput(attrs={'class': 'num_of'})
    )

    comments_video = forms.CharField(
        required=False,
        label='Comments on video',
        max_length=32,
        widget=forms.TextInput(attrs={'class': 'form-control', 'data-role': 'tagsinput'})
    )

    skip_top_posts = forms.BooleanField(required=False)

    users_to_like_posts = forms.CharField(
        required=False,
        label='Users',
        max_length=1024,
        widget=forms.TextInput(attrs={'class': 'form-control', 'data-role': 'tagsinput'})
    )

    amount_of_likes = forms.CharField(
        required=False,
        label='Amount of likes.',
        max_length=32,
        widget=forms.TextInput(attrs={'class': 'num_of'})
    )

    random_likes = forms.BooleanField(required=False)

    likes_of_likes = forms.CharField(
        required=False,
        label='Amount of likes.',
        max_length=32,
        widget=forms.TextInput(attrs={'class': 'num_of'})
    )

    randomize_posts_liked = forms.BooleanField(required=False)

    unfollow_if_inappropriate_tag = forms.BooleanField(required=False)

    interact_with_user = forms.BooleanField(required=False)

