from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect, render
from django.http import JsonResponse
# from RealEstate.form import *
from business.models import *

from django.core.exceptions import ObjectDoesNotExist


def home(request):
     information = Information.objects.all()
     about = About.objects.all()
     plan = businessplan.objects.all()
     services = Service.objects.all()
     reviews = Reviews.objects.all()
     customers = Ourcustomers.objects.all()
     Team = team.objects.all()
     blog = Blog.objects.all()
     chooseus = ChooseUs.objects.all()


     context = {
     'information':information,
     'about':about,
     'plan':plan,
     'services':services,
     'reviews':reviews,
     'customers':customers,
     'Team':Team,
     'blog':blog,
     'chooseus':chooseus
        }
     return render(request, 'index.html', context)



def Team(request):
     information = Information.objects.all()
     Team = team.objects.all()
     context = {'Team':Team,'information':information }
     return render(request, 'Team.html', context)


def about(request):
     about = About.objects.all()
     plan = businessplan.objects.all()
     customers = Ourcustomers.objects.all()
     Team = team.objects.all()
     information = Information.objects.all()
     chooseus = ChooseUs.objects.all()
     reviews = Reviews.objects.all()

     context = {'about':about,
     'information':information,
     'plan':plan,
     'customers':customers,
     'Team':Team,
     'chooseus':chooseus,
     'reviews':reviews,

}
     return render(request, 'AboutUs.html', context)


def CallUs(request):
     information = Information.objects.all()
     context = {'information':information}
     return render(request, 'CallUs.html', context)



def blog(request):
    blog_obj=Blog.objects.all()
    information = Information.objects.all()
    context = { 'blog_obj':blog_obj ,'information':information }
    return render(request, 'blog.html', context)



def blogdetails(request,id):

     blog_obj= get_object_or_404(Blog,id=id)
     information = Information.objects.all()
     blog = Blog.objects.all()



     context = {
     'blog_obj':blog_obj,
     'information':information,
     'blog':blog,
    }
     return render(request, 'blogdetails.html', context)
