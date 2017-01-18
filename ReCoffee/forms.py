from django import forms

class RegisterForm(forms.Form):
	userName = forms.CharField(label="Username")
	firstName = forms.CharField(label="First Name")
	lastName = forms.CharField(label="Last Name")
	passWord = forms.CharField(label="Password", widget=forms.PasswordInput)
	birthDay = forms.DateField(label='Birth Day', input_formats=['%Y-%m-%d'])

class LoginForm(forms.Form):
    username = forms.CharField(label="Username")
    password = forms.CharField(label="Password", widget=forms.PasswordInput)

class ReviewForm(forms.Form):
    text = forms.CharField(label="Leave review",
        widget=forms.Textarea)

class SearchForm(forms.Form):
    shop_name = forms.CharField(label="")
