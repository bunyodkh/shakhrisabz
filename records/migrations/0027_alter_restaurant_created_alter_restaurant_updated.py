# Generated by Django 4.2.6 on 2023-10-23 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0026_rename_case_attached_hotelimage_hotel_attached_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='created',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='updated',
            field=models.DateField(auto_now=True),
        ),
    ]
