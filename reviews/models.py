from django.db import models

# Create your models here.

class Review(models.Model):
    #author = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True)
    author = models.TextField()
    text = models.TextField()
    time = models.DateTimeField()    # auto_now = true
    stars = models.DecimalField(max_digits=2, decimal_places=1)
    # product = models.OneToOneField(Product, on_delete=models.SET_NULL)
    
class Product(models.Model):
    reviews = models.ManyToManyField(Review)
    desc = models.TextField()
    name = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    image = models.ImageField(upload_to='pics', null=True)



