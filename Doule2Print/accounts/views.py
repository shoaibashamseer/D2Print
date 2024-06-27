# accounts/views.py
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .models import UserProfile
from .forms import UserRegistrationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm


'''def register_retail(request):
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

'''
class CustomLoginView(LoginView):
    template_name = 'accounts/login.html'
    success_url = reverse_lazy('home')
def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            # Create a user profile with the selected customer type
            customer_type = form.cleaned_data['customer_type']
            UserProfile.objects.create(user=user, customer_type=customer_type)
            return redirect('login')  # Redirect to login page after successful registration
    else:
        form = UserRegistrationForm()
    return render(request, 'accounts/register.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('home')  # Redirect to the login page after logout

def profile(request):
    try:
        customer = request.user.UserProfile.customer
        # Now you can access customer attributes like customer.is_wholesale
        return render(request, 'profile.html', {'customer': customer})
    except UserProfile.DoesNotExist:
        # Handle the case where the user does not have a related customer profile
        return render(request, 'profile.html', {'error_message': 'User profile not found'})
