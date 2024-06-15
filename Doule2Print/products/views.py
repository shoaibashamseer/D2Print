from django.shortcuts import render, get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from .models import Product, Variety

from django.http import JsonResponse



#from .forms import CustomerForm, OrderForm

def home(request):
    products = Product.objects.all()
    return render(request, 'products/home.html', {'products': products})


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
'''
@login_required
def update_customer(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=request.user.customer)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CustomerForm(instance=request.user.customer)
    return render(request, 'products/update_customer.html', {'form': form})


@login_required
def order_product(request, variety_id):
    variety = get_object_or_404(Variety, id=variety_id)
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.customer = request.user.customer
            order.total_price = variety.retail_price * order.quantity if not request.user.customer.is_wholesale else variety.wholesale_price * order.quantity
            order.save()
            return redirect('home')
    else:
        form = OrderForm(initial={'variety': variety})
    return render(request, 'products/order_product.html', {'form': form, 'variety': variety})

@login_required
def place_order(request):
    if request.method == 'POST':
        variety_id = request.POST.get('variety_id')
        quantity = int(request.POST.get('quantity'))
        variety = Variety.objects.get(id=variety_id)
        customer = Customer.objects.get(user=request.user)
        if customer.is_wholesale:
            price = variety.wholesale_price
        else:
            price = variety.retail_price
        total_price = price * quantity
        order = Order.objects.create(customer=customer, variety=variety, quantity=quantity, total_price=total_price)
        return JsonResponse({'message': 'Order placed successfully!'})
    return JsonResponse({'error': 'Invalid request'}, status=400)'''

'''def place_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            product_id = form.cleaned_data['product']
            quantity = form.cleaned_data['quantity']
            product = Product.objects.get(pk=product_id)
            if product.stock >= quantity:
                # Decrease stock level
                product.stock -= quantity
                product.save()
                # Create order
                Order.objects.create(product=product, quantity=quantity)
                # Redirect or display success message
                return redirect('order_success')
            else:
                # Display error message
                form.add_error('quantity', 'Insufficient stock')
    else:
        form = OrderForm()
    return render(request, 'product_detail.html', {'form': form})'''
