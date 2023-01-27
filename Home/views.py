from django.shortcuts import render,HttpResponse
from datetime import datetime
from Home.models import Contact

# Create your views here.
# context={
#         "variable":"This is sent"
#     }
def index(request):
    return render(request, "index.html")
    # return HttpResponse("This is homepage")

def services(request):
    return render(request, "services.html")
    # return HttpResponse("This is service page")

def contact(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        contact=request.POST['contact']
        reason=request.POST['reason']
        contact=Contact(name=name,email=email,contact=contact,reason=reason,date=datetime.today())
        contact.save()
    return render(request, "contact.html")
     # return HttpResponse("This is contact page")

def about(request):
   return render(request, "about.html")
# return HttpResponse("This is about page")

def icecream(request):
   return render(request, "icecream.html")

def doughnut(request):
   return render(request, "doughnut.html")

def softy(request):
   return render(request, "softy.html")



