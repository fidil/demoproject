from django.shortcuts import render
from shop.models import Product
from django.db.models import Q

def searchresult(request):
    query=""
    products=None
    if(request.method=="post"):
        query=request.POST.get('q')
        # print(query)
        if(query):
            products=Product.objects.filter(Q(name__icontains=query) | Q(description__icontains=query))

    return render(request,'search.html',{'query':query,'products':products})
