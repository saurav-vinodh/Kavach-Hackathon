from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):
    if request.method == "POST":
        
        contact = request.POST[]

    return render(request, 'page.html')