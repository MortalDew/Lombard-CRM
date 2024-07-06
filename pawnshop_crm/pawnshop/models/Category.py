from django.db import models


class Category(models.Model):
    name = models.CharField(
        verbose_name='Имя категории',
        max_length=100,
        null=False,
        blank=False,
        default=None
    )
    interest_rate = models.DecimalField(
        verbose_name='Процентная ставка',
        max_digits=3,
        decimal_places=1,
        null=False,
        blank=False,
        default=None
    )

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return f'Категория \'{self.name}\''
