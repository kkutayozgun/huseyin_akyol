# Generated by Django 3.2 on 2022-07-10 18:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0002_auto_20220706_0756'),
    ]

    operations = [
        migrations.DeleteModel(
            name='HomePageSeoSlides',
        ),
        migrations.RemoveField(
            model_name='HomePageSeo',
            name='slides'
        )
    ]
