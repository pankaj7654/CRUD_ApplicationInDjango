from django.views import View
from django.shortcuts import render , redirect
from django.contrib.auth.hashers import make_password , check_password
from crud.models.user import User


class SignupView(View):
    def get(self , request):
        return render(request, 'signup.html')

    def post(self , request):
        try:
            name = request.POST.get('name')
            email = request.POST.get('email')
            phone = request.POST.get('phone')
            image = request.POST.get('photo')
            password = request.POST.get('password')           #Hashing password
            hashedPassword = make_password(password = password)
            user = User(name = name , email = email , image = image , password = hashedPassword , phone = phone)
            result = user.save()
            return render(request , 'login.html')
        except:
            return render(request, 'signup.html' , {'error' : "User Already Registered..."})
