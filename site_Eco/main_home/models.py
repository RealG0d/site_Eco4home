from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Plant(models.Model):

    tips = {
        ('Декоративно-лиственные растения', 'Декоративно-лиственные растения'),
        ('Красиво-цветущие растения', 'Красиво-цветущие растения'),
        ('Кактусы и суккуленты', 'Кактусы и суккуленты'),
    }

    name_plant = models.CharField(max_length=200, verbose_name='Название')
    type_plant = models.CharField(choices=tips, max_length=50, verbose_name='Вид растения')
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


class Quiz(models.Model):
    category_name = models.CharField(max_length=100, verbose_name='Категория')

    def __str__(self):
        return self.category_name


class Question(models.Model):
    category = models.ForeignKey(Quiz,
                                 related_name='Test',
                                 on_delete=models.CASCADE,
                                 verbose_name='Категория',
                                 )
    question = models.CharField(max_length=200, verbose_name='Вопрос')
    img_bg = models.ImageField(blank=True, upload_to='media', verbose_name='Картинка для вопроса')

    def __str__(self):
        return self.question

    def get_answers(self):
        answer_objs = list(Answer.odjects.filter(question=self))
        data = []
        for answer_obj in answer_objs:
            data.append({
                'answer': answer_obj.answer,
                'is_correct': answer_obj.is_correct,
            })


class Answer(models.Model):
    typs = {
        (1, 'Q1'),
        (2, 'Q2'),
        (3, 'Q3'),
    }

    question = models.ForeignKey(Question,
                                 related_name='question_answer',
                                 on_delete=models.CASCADE
                                 )
    answer = models.CharField(max_length=50, verbose_name='Ответ')
    is_correct = models.BooleanField(default=True)
    score_ans = models.IntegerField(choices=typs, verbose_name='Вариант ответа', default=1)

    def __str__(self):
        return self.answer
