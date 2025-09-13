from django.db import models

# Create your models here.

class NewProducts(models.Model):
      name = models.CharField(max_length=100, blank=True,null=True)
      img_url = models.TextField(blank=True,null=True)
      price = models.DecimalField(max_digits=10,decimal_places=2,default=0.00)
      description = models.TextField(blank=True,null=True)
      
      def __str__(self):
            return self.name