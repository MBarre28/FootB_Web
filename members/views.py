from django.template import loader
from django.shortcuts import render
from django.http import HttpResponse
from members.models import Member

def members(request):
    mymembers = Member.objects.all().values()
    template = loader.get_template('index.html')
    context = {
        'mymembers': mymembers,
        'link': 'link',
        'members' : 'members', 
    }
    return HttpResponse(template.render(context, request))

def details(request, id):
    mymember = Member.objects.get(id=id)
    template = loader.get_template('details.html')
    context = {
        'mymembers': mymember,
    }
    return HttpResponse(template.render(context, request))

def main(request):
    
    template = loader.get_template('main.html')
    context = {
        'link': 'link',
        'members' : 'members'     
    }
    
    return HttpResponse(template.render(context, request))


def nav(request):
    
    template = loader.get_template('nav.html')
    return HttpResponse(template.render())


def testing(request):
    
    template = loader.get_template('testing.html')
    context = {

        'greeting': 1,
        'firstname' : 'Muhammad',
        'lastname'  : 'Barre',
        'fruits' : [''],
    }
    return HttpResponse(template.render(context, request))
