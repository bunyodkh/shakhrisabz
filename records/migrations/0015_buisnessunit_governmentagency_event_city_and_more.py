# Generated by Django 4.2.6 on 2023-10-20 03:15

from django.db import migrations, models
import django.db.models.deletion
import location_field.models.plain


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0014_hotel_main_image_alter_hotelimage_created_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='BuisnessUnit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('created', models.DateField(auto_now_add=True)),
                ('updated', models.DateField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Бизнес',
                'verbose_name_plural': 'Бизнесы',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='GovernmentAgency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('created', models.DateField(auto_now_add=True)),
                ('updated', models.DateField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Государственное учреждение',
                'verbose_name_plural': 'Государственные учреждения',
                'ordering': ['-created'],
            },
        ),
        migrations.AddField(
            model_name='event',
            name='city',
            field=models.CharField(blank=True, default='Shahrisabz', max_length=255, null=True, verbose_name='Город'),
        ),
        migrations.AddField(
            model_name='event',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='event',
            name='event_type',
            field=models.CharField(blank=True, choices=[('Ad', 'Анонс'), ('Happening', 'Событие'), ('Event', 'Мероприятие')], default='Event', max_length=20, null=True, verbose_name='Тип'),
        ),
        migrations.AddField(
            model_name='event',
            name='location',
            field=location_field.models.plain.PlainLocationField(default='39.060366, 66.845915', max_length=63),
        ),
        migrations.AlterField(
            model_name='alert',
            name='created',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='alert',
            name='updated',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='created',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='title',
            field=models.CharField(max_length=100, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='event',
            name='updated',
            field=models.DateField(auto_now=True),
        ),
        migrations.CreateModel(
            name='EventImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to=None)),
                ('main', models.BooleanField(default=False, verbose_name='Главное изображение')),
                ('caption', models.CharField(blank=True, default='Изображение', max_length=200, null=True)),
                ('created', models.DateField(auto_now_add=True)),
                ('updated', models.DateField(auto_now=True)),
                ('case_attached', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='records.event')),
            ],
            options={
                'verbose_name': 'Изображение мероприятия',
                'verbose_name_plural': 'Изображения мероприятия',
                'ordering': ['caption'],
            },
        ),
    ]
