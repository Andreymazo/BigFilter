# Generated by Django 3.2.19 on 2023-09-09 18:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('big_filter', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studies',
            name='study_modality',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='big_filter.modalities', verbose_name='Модальность исследования'),
        ),
    ]
