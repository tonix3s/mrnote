# Generated by Django 2.2.10 on 2020-11-21 23:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='contact',
            field=models.CharField(max_length=264),
        ),
        migrations.AlterField(
            model_name='employee',
            name='name',
            field=models.CharField(max_length=264),
        ),
    ]
