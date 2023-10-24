# Generated by Django 4.2.6 on 2023-10-20 10:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0022_organization_delete_buisnessunit_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='organization',
            options={'ordering': ['-created'], 'verbose_name': 'Организация', 'verbose_name_plural': 'Организации'},
        ),
        migrations.AlterField(
            model_name='organization',
            name='org_type',
            field=models.CharField(blank=True, choices=[('government', 'Госучреждение'), ('business', 'Частный бизнес'), ('production', 'Производство'), ('service', 'Оказание услуг'), ('education', 'Образовательное учреждение'), ('others', 'Другие')], default='government', max_length=20, null=True, verbose_name='Тип организации'),
        ),
        migrations.CreateModel(
            name='OrganizationImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to=None)),
                ('main', models.BooleanField(default=False, verbose_name='Главное изображение')),
                ('caption', models.CharField(blank=True, max_length=200, null=True)),
                ('created', models.DateField(auto_now_add=True)),
                ('updated', models.DateField(auto_now=True)),
                ('case_attached', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='records.organization')),
            ],
            options={
                'verbose_name': 'Изображение организации',
                'verbose_name_plural': 'Изображения организации',
                'ordering': ['caption'],
            },
        ),
    ]
