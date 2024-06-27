from django.core.mail.backends import console
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from .models import Product, Variety

def home(request):
    products = Product.objects.all()
    varieties = Variety.objects.all()

    return render(request, 'products/home.html', {'products': products, 'varieties': varieties})


def product_detail(request, product_id):
    product = Product.objects.get(pk=product_id)
    varieties = product.varieties.all()

    context = {'product': product, 'varieties': varieties}
    if request.user.is_authenticated:
        if hasattr(request.user, 'customer') and request.user.customer.is_wholesale:
            for variety in varieties:
                variety.price = variety.wholesale_price
        else:
            for variety in varieties:
                variety.price = variety.retail_price  # assuming you have a retail_price field
    return render(request, 'products/product_detail.html', context)


def get_variety(request, variety_id):
    variety = get_object_or_404(Variety, id=variety_id)
    is_wholesale = request.user.customer.is_wholesale if request.user.is_authenticated and hasattr(request.user, 'customer') else False
    return JsonResponse({
        'id': variety.id,
        'name': variety.name,
        'description': variety.description,
        'image': variety.image.url,
        'retail_price': str(variety.retail_price),
        'wholesale_price': str(variety.wholesale_price),
        'stock': variety.stock,
        'is_wholesale': is_wholesale,
    })