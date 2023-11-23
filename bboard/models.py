from django.db import models


is_all_posts_passive = False
def is_active_default():
    return is_all_posts_passive
class Rubric(models.Model):
    name = models.CharField(max_length=20, db_index=True, verbose_name="Название", unique = True)


    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = 'Рубрики'
        verbose_name = 'Рубрика'
        ordering = ['name']


class Bb(models.Model):

    # KINDS = (
    #     ('Купля-продажа', (
    #         ('b', 'Куплю'),
    #         ('s', 'Продам'),
    #     )),
    #     ('Обмен', (
    #     ('c', 'Обменяю'),
    #     ))
    # )

    # KINDS = (
    #     ('b', 'Куплю'),
    #     ('s', 'Продам'),
    #     ('c', 'Обменяю'),
    # )
    KINDS = (
        (None, 'Выберите тип обьявления'),
        ('b', 'Куплю'),
        ('s', 'Продам'),
        ('c', 'Обменяю'),
    )

    # kind = models.CharField(max_lenght=1, choices=KINDS, default='s')
    kind = models.CharField(max_length=1, choices=KINDS, default='s')
    rubric = models.ForeignKey("Rubric", null=True, on_delete=models.PROTECT, verbose_name="Рубрика")
    title = models.CharField(max_length=50, verbose_name="Товар")
    content = models.TextField(null=True, blank=True, verbose_name="Описание")
    price = models.DecimalField(max_digits=8, decimal_places = 2, verbose_name= "Цена", default=0.0)
    is_active = models.BooleanField(default=is_active_default)
    published = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name="Опубликовано")
    email = models.SlugField(max_length =50, allow_unicode = True)
    # id = models.UUIDField(primary_key=True, default = uuid.uuid4, editable=False)
    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name_plural = 'Объявления'
        verbose_name = 'Объявление'
        ordering = ['-published']