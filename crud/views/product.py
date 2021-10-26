from django.views import View
from django.shortcuts import render , redirect
from crud.models.product import Product

class ProductView(View):
    def get(self , request):
        print("From Class Based View")
        products=Product.objects.all()
        context={
            "products":products,
        }
        return render(request, 'product.html', context=context)