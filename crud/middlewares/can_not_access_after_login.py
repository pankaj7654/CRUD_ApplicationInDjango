from django.shortcuts import render , redirect



def cantAccessAfterLogin(get_response):
    #index function pass here

    def middleware(request):
        user =  request.session.get('user')
        print(user,"user")
        if user:
            # if user got or already login then don't server page
            return redirect('index')
        else:
            return get_response(request)

    
    return middleware