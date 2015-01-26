from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    context_dict = {'boldmessage': "I am bold font from the context"}
    return render(request, 'rango/index.html', context_dict)
    #return HttpResponse("Rango says: Hello world! <br/> <a href='/rango/about'>About</a>")

def about(request):
    return render(request, 'rango/about.html')
    #return HttpResponse("This tutorial has been put together by Lorenzo Betto, 2083089b <br>Rango says here is the about page <br/> <a href='/rango'>Home</a>")
