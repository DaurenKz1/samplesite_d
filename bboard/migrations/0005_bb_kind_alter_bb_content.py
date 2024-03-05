# Generated by Django 4.2.7 on 2023-12-05 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bboard', '0004_alter_bb_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='bb',
            name='kind',
            field=models.CharField(choices=[('b', 'Куплю'), ('s', 'Продам'), ('c', 'Обменяю')], default='s', max_length=1),
        ),
        migrations.AlterField(
            model_name='bb',
            name='content',
            field=models.TextField(blank=True, default='Какое-то значение:', null=True, verbose_name='Описание'),
        ),
    ]
