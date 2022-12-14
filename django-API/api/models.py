from django.db import models

class Krosovka(models.Model):
    SPORT = 'SPORT'
    BAZM = 'BAZM'
    PRODUCT_FILTER = [
        (SPORT, 'Sport'),
        (BAZM, "Bazm")
    ]
    brand = models.CharField(max_length=100)
    size = models.IntegerField(default=10)
    color = models.CharField(max_length=30)
    price = models.IntegerField(default=40)
    turi = models.CharField( max_length=6, choices=PRODUCT_FILTER, default=SPORT)
    
    def __str__(self):
        return f"brand: {self.brand}"
