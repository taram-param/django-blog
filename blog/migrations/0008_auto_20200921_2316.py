# Generated by Django 3.1 on 2020-09-21 17:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20200918_0237'),
    ]

    operations = [
        migrations.AlterField(
            model_name='controlmodel',
            name='link_duration',
            field=models.DurationField(blank=True, default=datetime.timedelta(0, 30), verbose_name='activation time'),
        ),
        migrations.AlterField(
            model_name='controlmodel',
            name='name',
            field=models.CharField(default='duration', max_length=255, verbose_name='variable name'),
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
