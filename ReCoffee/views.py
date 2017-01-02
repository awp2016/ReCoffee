from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.views.generic.edit import DeleteView, UpdateView
from django.views.generic.list import ListView

from . import models
from . import forms

def index(request):
	context = {}
	return render (request, 'ReCoffee/home.html', context)

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
