# accounts/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomerForm
from .models import Customer

def register_retail(request):
    if request.method == 'POST':
        user_form = UserCreationForm(request.POST)
        customer_form = CustomerForm(request.POST)
        if user_form.is_valid() and customer_form.is_valid():
            user = user_form.save()
            customer = customer_form.save(commit=False)
            customer.user = user
            customer.is_wholesale = False  # Retail customer
            customer.save()
            login(request, user)
            return redirect('profile')
    else:
        user_form = UserCreationForm()
        customer_form = CustomerForm()
    return render(request, 'accounts/register_retail.html', {'user_form': user_form, 'customer_form': customer_form})

def register_wholesale(request):
    if request.method == 'POST':
        user_form = UserCreationForm(request.POST)
        customer_form = CustomerForm(request.POST)
        if user_form.is_valid() and customer_form.is_valid():
            user = user_form.save()
            customer = customer_form.save(commit=False)
            customer.user = user
            customer.is_wholesale = True  # Wholesale customer
            customer.save()
            login(request, user)
            return redirect('profile')
    else:
        user_form = UserCreationForm()
        customer_form = CustomerForm()
    return render(request, 'accounts/register_wholesale.html', {'user_form': user_form, 'customer_form': customer_form})

def profile(request):
    if not hasattr(request.user, 'customer'):
        return redirect('register_retail')
    return render(request, 'accounts/profile.html')


