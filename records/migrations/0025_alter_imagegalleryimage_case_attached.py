# Generated by Django 4.2.6 on 2023-10-20 10:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0024_imagegallery_alter_feedback_created_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagegalleryimage',
            name='case_attached',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='records.imagegallery'),
        ),
    ]
