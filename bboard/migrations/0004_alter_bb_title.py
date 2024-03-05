# Generated by Django 4.2.7 on 2023-11-30 13:53

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bboard', '0003_alter_bb_options_bb_is_active_bb_updated_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bb',
            name='title',
            field=models.CharField(error_messages={'invalid': 'Здесь могла быть ваша реклама!!!'}, max_length=50, validators=[django.core.validators.RegexValidator(regex='^.{4,}$')], verbose_name='Товар'),
        ),
    ]
