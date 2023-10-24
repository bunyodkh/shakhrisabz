# Generated by Django 4.2.6 on 2023-10-19 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0012_hotel_email_hotel_facebook_hotel_instagram_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guide',
            name='age',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Возраст'),
        ),
        migrations.AlterField(
            model_name='guide',
            name='daily_fee',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Стоимость услуг за день (в сумах)'),
        ),
        migrations.AlterField(
            model_name='guide',
            name='email',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Электронная почта'),
        ),
        migrations.AlterField(
            model_name='guide',
            name='first_name',
            field=models.CharField(max_length=100, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='guide',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=None, verbose_name='Фотография'),
        ),
        migrations.AlterField(
            model_name='guide',
            name='last_name',
            field=models.CharField(max_length=100, verbose_name='Фамилия'),
        ),
        migrations.AlterField(
            model_name='guide',
            name='middle_name',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Отчество'),
        ),
        migrations.AlterField(
            model_name='guide',
            name='phone',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Телефон'),
        ),
        migrations.AlterField(
            model_name='guide',
            name='sex',
            field=models.CharField(blank=True, choices=[('Male', 'Мужчина'), ('Female', 'Женщина')], default='Male', max_length=20, null=True, verbose_name='Пол'),
        ),
        migrations.AlterField(
            model_name='hotel',
            name='city',
            field=models.CharField(blank=True, default='Shahrisabz', max_length=255, null=True, verbose_name='Город'),
        ),
        migrations.AlterField(
            model_name='hotel',
            name='description',
            field=models.TextField(blank=True, max_length=1000, null=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='hotel',
            name='email',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Электронная почта'),
        ),
        migrations.AlterField(
            model_name='hotel',
            name='facebook',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Фейсбук'),
        ),
        migrations.AlterField(
            model_name='hotel',
            name='instagram',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Инстаграм'),
        ),
        migrations.AlterField(
            model_name='hotel',
            name='phone',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Телефон'),
        ),
        migrations.AlterField(
            model_name='hotel',
            name='telegram',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Телеграм'),
        ),
        migrations.AlterField(
            model_name='hotel',
            name='title',
            field=models.CharField(max_length=100, verbose_name='Название'),
        ),
    ]
