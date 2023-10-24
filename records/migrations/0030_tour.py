# Generated by Django 4.2.6 on 2023-10-23 11:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0029_remove_transport_title_transport_driver_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tour',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=600, verbose_name='Название')),
                ('description', models.TextField(max_length=1000, verbose_name='Описание')),
                ('image', models.ImageField(blank=True, null=True, upload_to=None)),
                ('price', models.CharField(max_length=50, verbose_name='Цена')),
                ('address', models.CharField(max_length=200, verbose_name='Адрес')),
                ('notes', models.TextField(blank=True, null=True, verbose_name='Дополнительная информация')),
                ('active', models.BooleanField(default=False, verbose_name='Активно')),
                ('created', models.DateField(auto_now_add=True)),
                ('updated', models.DateField(auto_now=True)),
                ('company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='records.organization')),
            ],
            options={
                'verbose_name': 'Тур',
                'verbose_name_plural': 'Туры',
                'ordering': ['-created'],
            },
        ),
    ]
