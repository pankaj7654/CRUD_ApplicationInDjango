from django.views import View
from django.shortcuts import render , redirect
from crud.models.product import Product

class ProductDeleteView(View):
    def get(self , request,product_id):
        user = request.session.get('user')
        if user:
            product = Product.objects.get(id=product_id)
            product.delete()

            return redirect('product-view')
        else:
            return render(request, 'login.html')