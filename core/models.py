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
    material_for_build = models.ForeignKey(Material, related_name='Buildings_can_be_build')
    materials_produce = models.ForeignKey(Material, related_name='Buildings_can_produce')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'здание'
        verbose_name_plural = 'здания'
