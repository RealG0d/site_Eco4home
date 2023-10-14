from django.db import models

class Plant(models.Model):
    name_plant = models.CharField(max_length=200)
    type_plant = models.CharField(max_length=50)
    price_plant = models.IntegerField()
    img_plant = models.ImageField()
    text_plant = models.TextField()

    def __str__(self):
        return self.name_plant
