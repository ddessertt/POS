from django.db import models

# Create your models here.
class Type(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200, null=True)

    def __str__(self):
        return '%s (%s)' %(self.name, self.description)

class Product(models.Model):
    name = models.CharField(max_length=50)
    Type = models.ForeignKey(Type, on_delete=models.CASCADE, default='', null=True)
    description = models.CharField(max_length=200, null=True)
    price = models.IntegerField(default=0)

    def __str__(self):
        return '%s (%s) %d฿' %(self.name, self.Type, self.price)