from django.shortcuts import render

def home(request):
    #return HttpResponse("Tech Duo")
    return render(request, 'home.html')