from django.views import View
from django.shortcuts import render , redirect
from crud.models.product import Product
from crud.models.user import User

class ProductView(View):
    def get(self , request):
        user =  request.session.get('user')
        print(type(user))

        userojb = User.objects.get(email=user['email'])
        print(type(userojb))

        # product = product.object.get()
        products = Product.objects.filter(user=userojb)
       
        # products=Product.objects.all()
        context={
            "products":products,
            "user":user
        }
        return render(request, 'product.html', context=context)
