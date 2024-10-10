from django.db import models #type:ignore
class Items(models.Model):
    ProductID=models.CharField(max_length=20)
    url=models.URLField(max_length=200)
    ProductName=models.CharField(max_length=20)
    productPrice=models.CharField(max_length=20)
    DiscountPrice=models.CharField(max_length=20)

def __str__(self):
    return self.ProductID,self.url,self.ProductName,self.productPrice,self.DiscountPrice

    





