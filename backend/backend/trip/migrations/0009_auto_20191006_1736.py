# Generated by Django 2.2.6 on 2019-10-06 17:36

import colorfield.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trip', '0008_tripcategory_color'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tripcategory',
            name='color',
            field=colorfield.fields.ColorField(max_length=18, null=True, verbose_name='color'),
        ),
    ]