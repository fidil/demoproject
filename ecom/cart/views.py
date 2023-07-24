from django.shortcuts import render,redirect
from shop.models import Product
from cart.models import Cart
def add_cart(request,p):
    product=Product.objects.get(id=p)
    user=request.user
    try:
        cart=Cart.objects.get(products=product,user=user)
        if cart.quantity<cart.products.stock:
            cart.quantity+=1
        cart.save()

    except Cart.DoesNotExist:
        cart=Cart.objects.create(user=user,products=product,quantity=1)
        cart.save()

    return redirect("cart:cartview")

def cartview(request):
    user=request.user
    try:
        cart=Cart.objects.filter(user=user)

    except Cart.DoesNotExist:
        pass
    return render(request,'cart.html',{'cart':cart})