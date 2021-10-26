from django.shortcuts import render, HttpResponse , redirect
from crud.models.user import User
from urllib.parse import urlencode



# filter data from databse and send data on index.html page
def index(request):

    return render(request, 'index.html')



# clear session 
def logout(request):
    request.session.clear()
    return redirect('index') #name of index url

