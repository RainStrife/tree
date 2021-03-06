# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-15 00:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Building',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
            ],
            options={
                'verbose_name_plural': 'здания',
                'verbose_name': 'здание',
            },
        ),
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
            ],
            options={
                'verbose_name_plural': 'материалы',
                'verbose_name': 'материал',
            },
        ),
        migrations.AddField(
            model_name='building',
            name='materials_for_build',
            field=models.ManyToManyField(blank=True, related_name='buildings_can_be_build', to='core.Material', verbose_name='Материалы для постройки'),
        ),
        migrations.AddField(
            model_name='building',
            name='materials_produce',
            field=models.ManyToManyField(related_name='buildings_can_produce', to='core.Material', verbose_name='Материалы которые производит'),
        ),
    ]
