from django.views import View
from django.shortcuts import render , redirect , HttpResponse
from django.contrib.auth.hashers import check_password , make_password
from crud.models.user import User
from crud.utils.email_sender import sendEmail
import math
import random



# set new password
class ResetPassword(View):
    def get(self , request):
        return render(request , 'reset-password.html' , {'step1' : True})


    def post(self , request):
        pass
        password = request.POST.get('password')
        repassword = request.POST.get('repassword')
        error = None
        if len(password) < 6:
            error = 'Password must be more than 6 char long'

        elif len(repassword) < 6:
            error = 'Password must be more than 6 char long'

        elif password != repassword:
            error = 'Password miss matched'

        if error:
            return render(request, 'reset-password.html' , {'step3' : True , 'error' : error})
        else:
            email = request.session.get('reset-password-email')
            user = User.objects.get(email = email)
            user.password = make_password(password)
            user.save()
            request.session.clear()
            sendEmailAfterChangePassword(user)
            return render(request , 'login.html' , {'message' : 'Password Changed...'})



def sendEmailAfterChangePassword(user):
    html = "<h1>Password Changed Successfully....</h1>"
    sendEmail(user.name , user.email , message='Password Changed' , htmlContent=html , subject='Password Changed Successfully')



# code verify reset password code

def verifyResetPasswordCode(request):
    code =  request.POST.get('code')
    sessioncode = request.session['reset-password-verification-code']
    if code == str(sessioncode):
        return render(request, 'reset-password.html' , {'step3' : True})
    else:
        return render(request, 'reset-password.html' , {'step2' : True})


# change password

class PasswordResetVerification(View):
    def post(self , request):
        print(request.POST.get('email'))
        email = request.POST.get('email')
        try:
            user = User.objects.get(email = email)
            print(user)
            otp = math.floor(random.random() * 10000000)

            html = f'''

            <h4>Your Password Reset Verification Code is {otp}

            '''

            sendEmail(name = "User" , email=email  , subject = 'Reset Password Verification Code' , message= "Password Reset Verification Code" , htmlContent=html)
            request.session['reset-password-verification-code'] = otp
            request.session['reset-password-email'] = email
            print(otp)
            print(email)
            return render(request, 'reset-password.html' , {'step2' : True})

        except:
            return redirect('/reset-password') # we can redirect from url as wel as name of url