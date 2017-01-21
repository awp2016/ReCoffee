from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.core.urlresolvers import reverse
from django.views.generic.edit import DeleteView, UpdateView
from django.views.generic.list import ListView
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.db.models import Q
from django.http import HttpResponseRedirect

from . import models
from models import UserProfile
from . import forms
import json


def index(request):
    form = forms.SearchForm()
    context = {'form': form, }
    return render(request, 'ReCoffee/home.html', context)


def register_view(request):
    context = {}
    if request.method == 'POST':
        formular = forms.RegisterForm(request.POST)
        if formular.is_valid():
            userName = formular.cleaned_data['userName']
            passWord = formular.cleaned_data['passWord']
            firstName = formular.cleaned_data['firstName']
            lastName = formular.cleaned_data['lastName']
            birthDay = formular.cleaned_data['birthDay']
            userNou = User.objects.create_user(username = userName, password = passWord)
            userProfil = UserProfile.objects.create(first_name = firstName,last_name = lastName,birthday = birthDay,user = userNou)
            return HttpResponseRedirect("/")
    elif request.method == 'GET':
        formular = forms.RegisterForm()
    context['formularul'] = formular
    return render(request, 'ReCoffee/register.html', context)
    



def login_view(request):
    context = {}
    if request.method == 'GET':
        form = forms.LoginForm()
    elif request.method == 'POST':
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'])
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
        user_profile = models.UserProfile.objects.get(pk=pk)
    context = {'user_profile': user_profile, }
    return render(request, 'ReCoffee/user_profile.html', context)


def shop_profile(request, pk):
    form = forms.ReviewForm()
    context = {'form': form, }
    if request.method == 'GET':
        shop_profile = models.ShopProfile.objects.get(pk=pk)
    context = {'shop_profile': shop_profile, }
    return render(request, 'ReCoffee/shop_profile.html', context)
'''
def add_favorite(request):
    context = {}
    if request.method == 'POST':
        fav = forms.RegisterForm(request.POST)
        if fav.is_valid():
            userName = formular.cleaned_data['userName']
            shopProfile = formular.cleaned_data['shopProfile']
    context['fav'] = fav
    return render(request, 'ReCoffee/user_profile.html', context)
'''


def search_view(request):
    context = {}
    p = []
    listaCafenele = []
    if request.method == 'GET':
        shopform = forms.SearchForm()
    elif request.method == 'POST':
        shopform = forms.SearchForm(request.POST)
        if shopform.is_valid():
            shopSearch = shopform.cleaned_data['shopSearch']
            p = ShopProfile.objects.get(
                Q(name__icontains=shopSearch) | Q(location__icontains=shopSearch))
            for i in p:
                listaCafenele.append(i.name)
            return JsonResponse(listaCafenele)

    context['shopform'] = shopform
    return render(request, 'ReCoffee/results.html', context)
