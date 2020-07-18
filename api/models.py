from django.db import models
from tastypie.resources import ModelResource
from members.models import Member

# Create your models here.

class Membersapi(ModelResource):
    class Meta:
        queryset = Member.objects.all()
        resource_name='members'

