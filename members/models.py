from django.db import models

class Member(models.Model):
    firstname = models.CharField(max_length= 100)
    lastname = models.CharField(max_length= 100)
    phone = models.IntegerField(null=True)
    joined_date = models.DateField(auto_now_add=True)


    def __str__(self):
        return f"{self.firstname}, {self.lastname}"
    
