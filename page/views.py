from django.shortcuts import render
from django.http.response import HttpResponse
from django.template import Context,loader
from page.models import *

# Create your views here.

def homeindex(request):
    return render(request,'page/home.html',{'navbar':Navbarhome.objects.all(),'servicesitem':ServicesNavbar.objects.all(),'image':BackgroundImage.objects.all(),'home':Home.objects.all(),'footer':Footer.objects.all()})

def aboutusindex(request):
    return render(request,'page/aboutus.html',{'navbar':Navbarhome.objects.all(),'servicesitem':ServicesNavbar.objects.all(),'about':Aboutus.objects.all(),'aboutpara':Aboutusparagrap.objects.all(),'aboutimg':Aboutusimage.objects.all(),'footer':Footer.objects.all()})

def projectsindex(request):
    return render(request,'page/projects.html',{'navbar':Navbarhome.objects.all(),'servicesitem':ServicesNavbar.objects.all(),'projects':Projects.objects.all(),'gallery':Galleryprojects.objects.all(),'footer':Footer.objects.all()})

def contactusindex(request):
    return render(request,'page/contactus.html',{'navbar':Navbarhome.objects.all(),'servicesitem':ServicesNavbar.objects.all(),'contactus':Contactus.objects.all(),'info':InfoContactus.objects.all(),'map':MapContactus.objects.all(),'footer':Footer.objects.all()})

def acrylicindex(request):
    return render(request,'page/acrylic.html',{'navbar':Navbarhome.objects.all(),'servicesitem':ServicesNavbar.objects.all(),'services':Services.objects.all(),'footer':Footer.objects.all()})

def epoxyindex(request):
    return render(request,'page/epoxy.html',{'navbar':Navbarhome.objects.all(),'servicesitem':ServicesNavbar.objects.all(),'services':Services.objects.all(),'footer':Footer.objects.all()})

def polishindex(request):
    return render(request,'page/polish.html',{'navbar':Navbarhome.objects.all(),'servicesitem':ServicesNavbar.objects.all(),'services':Services.objects.all(),'footer':Footer.objects.all()})

def stainindex(request):
    return render(request,'page/stain.html',{'navbar':Navbarhome.objects.all(),'servicesitem':ServicesNavbar.objects.all(),'services':Services.objects.all(),'footer':Footer.objects.all()})



