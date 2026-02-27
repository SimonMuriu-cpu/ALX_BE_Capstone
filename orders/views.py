from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Order
from products.models import Product
from .models import OrderItem

@login_required
def orders_list(request):
    if request.user.role == "ADMIN":
        orders = Order.objects.all()
    elif request.user.role == "INTERMEDIARY":
        orders = Order.objects.all()
    else:
        orders = Order.objects.filter(user=request.user)

    return render(request, "orders/orders_list.html", {"orders": orders})


@login_required
def create_order(request):
    if request.method == "POST":
        product_id = request.POST.get("product")
        quantity = int(request.POST.get("quantity"))
        product = Product.objects.get(id=product_id)

        if product.available_quantity >= quantity:
            order = Order.objects.create(user=request.user)
            OrderItem.objects.create(
                order=order,
                product=product,
                quantity=quantity,
                price_at_order_time=product.price
            )
            product.available_quantity -= quantity
            product.save()
            return redirect("orders_list")

    products = Product.objects.all()
    return render(request, "orders/create_order.html", {"products": products})