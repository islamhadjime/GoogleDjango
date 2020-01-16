from django.shortcuts import render
from .googleSearch import *
from django.http import HttpResponse
from .forms import UserForm



def post_list(request):
    if request.method == "POST":
        name = request.POST.get("name")
        result = googleSearch(name).update()
        return render(request,'newSite/result.html',{"names":name,"parses":result})
    else:
        userform = UserForm()
        return render(request, "newSite/index.html", {"form": userform})










def about(request):
    return render(request,'newSite/about.html')

def contact(request):
    return render(request,'newSite/contact.html')
