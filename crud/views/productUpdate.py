from django.views import View
from django.shortcuts import render , redirect
from crud.models.product import Product

class ProductUpdateView(View):
    def get(self , request, product_id):
        print("From Class Based View")
        user = request.session.get('user')
        product = Product.objects.get(id=product_id)
        print(product,"RRRRRRRRRRRRRRRRrr")
        context={
            "product":product,
            "user":user
        }
        return render(request, 'productUpdate.html', context=context)
        

    def post(self , request, product_id):
        productname = request.POST.get('productname')
        quantity = request.POST.get('quantity')
        description = request.POST.get('description')
        price = request.POST.get('price')

        productObj = Product.objects.get(id=product_id)
        productObj.name=productname
        productObj.quantity=quantity
        productObj.description=description
        productObj.price=price
        productObj.save()

        user = request.session.get('user')
        product = Product.objects.get(id=product_id)
        context={
            "product":product,
            "user":user,
            "message":"Successfully Updated"
        }
        return render(request, 'productUpdate.html', context=context)
