from django.db import models


# Create your models here.
class housedetail(models.Model):
    mid = models.AutoField
    bedrooms = models.IntegerField()
    bathrooms = models.IntegerField()
    area = models.CharField(max_length=30)
    expected_rent = models.CharField(max_length=50)
    expected_advance = models.CharField(max_length=50)
    image = models.ImageField(upload_to="houseowner/images")



