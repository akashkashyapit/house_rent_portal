from django.db import models


# Create your models here.



class TicketGenerate(models.Model):
    uname = models.CharField(max_length=30)
    email = models.EmailField(max_length=100)
    message = models.TextField(max_length=400)
    status = models.CharField(max_length=30, default="Created")
    reply = models.CharField(max_length=200, default="")

    def __str__(self):
       return self.email