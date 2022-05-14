from django.db import models

# Create your models here.
class District(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name



class Seller(models.Model):
    name = models.CharField(max_length=250)
    district = models.ForeignKey(District, on_delete=models.CASCADE)

    def __str__(self):
        return self.name



class Customer(models.Model):
    name = models.CharField(max_length=100)
    mobileno = models.IntegerField()
    address = models.CharField(max_length=250)
    pincode = models.IntegerField()
    district = models.ForeignKey(District, on_delete=models.SET_NULL, null=True)
    seller = models.ForeignKey(Seller, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name
