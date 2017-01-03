from django import forms

class LoginForm(forms.Form):
	username = forms.CharField(label="Username")
	password = forms.CharField(label="Password", widget=forms.PasswordInput)

class ReviewForm(forms.Form):
	text = forms.CharField(label="Leave review", widget=forms.Textarea)

class SearchForm(forms.Form):
	shop_name = forms.CharField(label="")
