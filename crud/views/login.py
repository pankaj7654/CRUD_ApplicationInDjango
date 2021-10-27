from django.views import View
from django.shortcuts import render , redirect
from django.contrib.auth.hashers import check_password , make_password
from crud.models.user import User

class LoginView(View):
    def get(self , request):
        return_url = None
        print("From Class Based View")
        LoginView.return_url = request.GET.get('return_url')
        return render(request, 'login.html')


    def post(self , request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        print(email, password)
        try:
            user = User.objects.get(email = email)
            flag = check_password(password = password , encoded = user.password)
            print(flag)
            if flag:
                #collect Products
                temp = {}
                temp['email'] = user.email
                temp['id'] = user.id
                request.session['user'] = temp
                if LoginView.return_url:
                    return redirect(LoginView.return_url)
                context={
                    'user':user
                }
                print(user,"kkkkkkkkkkkkkkkkkkkkkkkk")
                print(user.id,"PPPPPPPPPPPPPPPPPPPPPPPPPPP")
                return render(request, 'index.html', context=context) #redirect index from url name
            else:
                return render(request, 'login.html' , {'error' : 'Please Enter Valide Email or Password'})        
            
        except:
            return render(request, 'login.html' , {'error' : 'Please Enter Valide Email or Password'})
            