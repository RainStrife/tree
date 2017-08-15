from django.db import models


# Create your models here.
class Material(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'материал'
        verbose_name_plural = 'материалы'


class Building(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')
    materials_for_build = models.ManyToManyField(Material, blank=True, related_name='buildings_can_be_build', verbose_name='Материалы для постройки')
    materials_produce = models.ManyToManyField(Material, related_name='buildings_can_produce', verbose_name='Материалы которые производит')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'здание'
        verbose_name_plural = 'здания'
