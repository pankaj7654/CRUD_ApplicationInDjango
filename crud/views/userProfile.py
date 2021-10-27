from django.views import View
from django.shortcuts import render , redirect
from crud.models.user import User

class UserProfile(View):
    def get(self , request, user_id):
        user = request.session.get('user')
        profile = User.objects.get(id=user.get('id'))
        context = {
            'profile' : profile,
            'user':user
        }
        return render(request, 'userProfile.html', context=context)
