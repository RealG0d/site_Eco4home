from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Plant(models.Model):
    name_plant = models.CharField(max_length=200, verbose_name='Название')
    type_plant = models.CharField(max_length=50, verbose_name='Вид растения')
    price_plant = models.IntegerField(verbose_name='Цена',
                                      validators=[
                                          MinValueValidator(1),
                                      ]
                                      )
    img_plant = models.ImageField(blank=True, upload_to='media', verbose_name='Картинка товара')
    text_plant = models.TextField(verbose_name='Описание товара')
    sale_plant = models.IntegerField(blank=True,
                                     verbose_name='Процент скидки',
                                     default=0,
                                     validators=[
                                         MaxValueValidator(100),
                                         MinValueValidator(0),
                                     ]
                                     )

    def __str__(self):
        return self.name_plant

    def get_sale(self):
        new_price = int(self.price_plant * (100 - self.sale_plant) / 100)
        return new_price
