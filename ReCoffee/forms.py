from django import forms


class RegisterForm(forms.Form):
    userName = forms.CharField(label="Username",widget=forms.TextInput(attrs={'placeholder': 'username'}))
    firstName = forms.CharField(label="First Name",widget=forms.TextInput(attrs={'placeholder': 'Prenume'}))
    lastName = forms.CharField(label="Last Name",widget=forms.TextInput(attrs={'placeholder': 'Nume'}))
    passWord = forms.CharField(label="Password", widget=forms.PasswordInput)
    birthDay = forms.DateField(label="Birth Day", input_formats=['%d-%m-%Y'],widget=forms.TextInput(attrs={'placeholder': 'Day-Mon-Year'}))


class LoginForm(forms.Form):
    username = forms.CharField(label="Username")
    password = forms.CharField(label="Password", widget=forms.PasswordInput)


class ReviewForm(forms.Form):
    text = forms.CharField(label="Leave review",
                           widget=forms.Textarea)
    rating = forms.ChoiceField(choices=[(x, x) for x in range(1, 11)],label="Rating")

class FavoriteForm(forms.Form):
    username = forms.CharField(label="Username")
    shopprofile = forms.CharField(label="Shop")


class SearchForm(forms.Form):
    shopSearch = forms.CharField(label="Cauta")
