from django.views import View
from django.shortcuts import render , redirect
from crud.models.user import User

class UserProfileUpdate(View):
    def get(self , request, user_id):
        user = request.session.get('user')
        profile = User.objects.get(id=user.get('id'))
        context = {
            'profile' : profile,
            'user':user
        }
        return render(request, 'userProfileUpdate.html', context=context)
    

    def post(self , request, user_id):
        name = request.POST.get('name')
        phone = request.POST.get('phone')

        user = request.session.get('user')
        profileObj = User.objects.get(id=user.get('id'))
        profileObj.name=name
        profileObj.phone=phone

        profileObj.save()

        user = request.session.get('user')
        profile = User.objects.get(id=user.get('id'))
        context = {
            'profile' : profile,
            'user':user,
            "message":"Profile Updated Successfully"
        }
        return render(request, 'userProfile.html', context=context)