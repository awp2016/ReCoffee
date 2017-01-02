from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.core.urlresolvers import reverse
from django.views.generic.edit import DeleteView, UpdateView
from django.views.generic.list import ListView

from . import models
from . import forms

def index(request):
	form = forms.SearchForm()
	context = {'form':form,}
	return render(request, 'ReCoffee/home.html', context)

def login_view(request):
	context = {}
	if request.method == 'GET':
		form = forms.LoginForm()
	elif request.method == 'POST':
		form = forms.LoginForm(request.POST)
		if form.is_valid():
			user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
			if user:
				login(request=request, user=user)
				return redirect('index')
			else:
				context['error_message'] = 'Wrong username or password!'
	context['form'] = form
	return render(request, 'ReCoffee/login.html', context)

def logout_view(request):
	if request.method == 'GET':
		logout(request)
		return redirect('index')

def user_profile(request, pk):
	if request.method == 'GET':
		user_pofile = models.UserProfile.objects.get(pk=pk)
	context = {'user_profile': user_profile,}
	return render(request, 'ReCoffee/user_profile.html', context)

def shop_profile(request, pk):
	if request.method == 'GET':
		shop_profile = models.ShopProfile.objects.get(pk=pk)
	context = {'shop_profile': shop_profile,}
	return render(request, 'ReCoffee/shop.html', context)


'''
def search_view(request):
	context = {}
	if request.method == 'GET':
		form = forms.SearchForm()
	elif request.method == 'POST':
		form = forms.SearchForm(request.POST)
		if form.is_valid():
			search = 
	context['form'] = form
	return render(request, 'ReCoffee/results.html', context)
'''
