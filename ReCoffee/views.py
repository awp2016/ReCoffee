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
from django.core.exceptions import ObjectDoesNotExist

from . import models
from . import forms
import json


def index(request):
    context = {}

    # modificare by bogdan
    rate = models.ShopProfile.objects.all().order_by('rating').reverse()
    context['rate'] = rate
    # end modificare bogdan

    if request.method == 'GET':
        form = forms.SearchForm()
    elif request.method == 'POST':
        form = forms.SearchForm(request.POST)
        if form.is_valid():
            shopSearch = form.cleaned_data['shopSearch']
            return redirect('lista_cafenele', shopSearch)

    context['form'] = form
    return render(request, 'ReCoffee/home.html', context)


def lista_cafenele_view(request, shopSearch):
    context = {}
    lista = models.ShopProfile.objects.filter(name__icontains=shopSearch)
    if not lista:
        context['errormessage'] = 'Not found!'
    else:
        context['listaCafenele'] = lista
    return render(request, 'ReCoffee/lista_cafenele.html', context)


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
            userNou = User.objects.create_user(
                username=userName, password=passWord)
            userProfil = models.UserProfile.objects.create(
                first_name=firstName, last_name=lastName,
                birthday=birthDay, user=userNou)
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

    # if not is_safe_url(url=redirect_to, host=request.get_host()):
    #redirect_to = request.POST.get('next', request.GET.get('next', '/'))
    return render(request, 'ReCoffee/login.html', context)


def logout_view(request):
    if request.method == 'GET':
        logout(request)
        return redirect('index')


def user_profile(request, pk):
    user_profile = models.UserProfile.objects.get(pk=pk)
    fave_list = user_profile.favorite.all()
    context = {'user_profile': user_profile, 'fave_list': fave_list, }
    return render(request, 'ReCoffee/user_profile.html', context)


def shop_profile(request, pk):
    context = {}
    shop = models.ShopProfile.objects.get(pk=pk)
    review_list = models.Review.objects.filter(shop=shop)
    user_profile = models.UserProfile.objects.get(user=request.user)


    try:
        exist = models.Favorite.objects.get(user=user_profile, shop=shop)
        flag = True
    except ObjectDoesNotExist:
        flag = False

    if request.method == 'GET':
        form = forms.ReviewForm()
    if request.method == 'POST':
        form = forms.ReviewForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['text']
            rating = form.cleaned_data['rating']
            last_rating = shop.rating

            shop.rating = (last_rating + int(rating)) / 2
            shop.save()

            review = models.Review(text=text, author=user_profile, shop=shop)
            review.save()

            return redirect('shop_profile', shop.pk)

    context['shop'] = shop
    context['form'] = form
    context['review_list'] = review_list
    context['flag'] = flag
    return render(request, 'ReCoffee/shop_profile.html', context)


def add_fave(request, shop_pk):
    user = request.user
    profile = models.UserProfile.objects.get(user=user)
    shop = models.ShopProfile.objects.get(pk=shop_pk)
    new_fave = models.Favorite(user=profile, shop=shop)
    new_fave.save()

    return redirect('user_profile', profile.pk)
