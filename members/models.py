from django.db import models

class Name(models.Model):
    name = models.CharField(max_length=250,blank=True)

    def __str__(self):
        return self.name


class Member(models.Model):
    designation = models.CharField(max_length=250)
    join_year= models.IntegerField(blank=True)
    last_year= models.IntegerField(blank=True)
    name =models.ForeignKey(Name,on_delete=models.CASCADE)

    # def __str__(self):
    #     return self.designation