from django.views import View
from django.shortcuts import render , redirect
from crud.models.product import Product

class ProductInsertView(View):
    def get(self , request):
        user = request.session.get('user')
        context={
            "user":user
        }
        return render(request, 'productInsert.html', context=context)

    def post(self , request):
        productname = request.POST.get('productname')
        quantity = request.POST.get('quantity')
        description = request.POST.get('description')
        price = request.POST.get('price')

        productObj=Product(name=productname,description=description,quantity=quantity,price=price)
        
        productObj.save()

        user = request.session.get('user')
        context={
            "user":user,
            "message":"Successfully inserted"
        }
        return render(request, 'productInsert.html', context=context)
