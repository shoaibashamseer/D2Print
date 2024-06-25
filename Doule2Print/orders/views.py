from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from .models import Order
from .forms import OrderForm
from products.models import Variety
from accounts.models import Customer

'''def place_order(request, variety_id):
    variety = get_object_or_404(Variety, id=variety_id)



    if not hasattr(request.user, 'customer'):
        # Handle missing customer profile
        return redirect('create_customer_profile')  # Redirect to a profile creation page or show an error message

    customer = request.user.customer
    is_wholesale = customer.is_wholesale

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.customer = request.user
            order.variety = variety
            order.total_price = order.quantity * (variety.wholesale_price if is_wholesale else variety.retail_price)

            if order.quantity > variety.stock:
                return JsonResponse({'status': 'error', 'message': 'Insufficient stock available'}, status=400)

            order.save()
            variety.stock -= order.quantity
            variety.save()
            return JsonResponse({'status': 'success'})
        else:
            return JsonResponse({'status': 'error', 'errors': form.errors}, status=400)
    else:
        form = OrderForm()
        return render(request, 'orders/place_order.html', {
        'form': form,
        'variety': variety,
        'is_wholesale': is_wholesale,
        'stock': variety.stock,
    })
'''

def place_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        variety_id = request.POST.get('variety_id')
        variety = get_object_or_404(Variety, id=variety_id)

        if not hasattr(request.user, 'customer'):
            return JsonResponse({'status': 'error', 'message': 'User has no customer profile'}, status=400)

        customer = request.user.customer
        is_wholesale = customer.is_wholesale

        if form.is_valid():
            order = form.save(commit=False)
            order.customer = customer
            order.variety = variety
            order.total_price = order.quantity * (variety.wholesale_price if is_wholesale else variety.retail_price)

            if order.quantity > variety.stock:
                return JsonResponse({'status': 'error', 'message': 'Insufficient stock available'}, status=400)

            order.save()
            variety.stock -= order.quantity
            variety.save()
            return JsonResponse({'status': 'success'}, status=200)
        else:
            return JsonResponse({'status': 'error', 'errors': form.errors}, status=400)
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=400)


def get_variety(request, variety_id):
    variety = get_object_or_404(Variety, id=variety_id)
    return JsonResponse({
        'id': variety.id,
        'name': variety.name,
        'description': variety.description,
        'image': variety.image.url,
        'retail_price': str(variety.retail_price),
        'wholesale_price': str(variety.wholesale_price),
        'stock': variety.stock,
    })