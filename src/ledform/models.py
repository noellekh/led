from django.db import models
from django.urls import reverse

# Create your models here.
class Product(models.Model):
    titre = models.CharField(max_length=120)
    description = models.TextField(blank =True, null=True)
    prix = models.DecimalField(decimal_places=2, max_digits=1000)
    resume = models.TextField()
    featured = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse("products:product-detail", kwargs={"id": self.id})
    