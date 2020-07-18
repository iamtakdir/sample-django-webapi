from django.shortcuts import render
from .models import*
from django.http import HttpResponse
# Create your views here.

def Team (request):
    members =Member.objects.all()

    return render (request, 'members/team.html',{'members':members}) 


def details (request,member_id):
    member = Member.objects.get(pk=member_id)
    return render (request,'members/details.html',{'member':member})