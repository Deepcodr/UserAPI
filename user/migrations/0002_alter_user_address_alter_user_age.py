# Generated by Django 4.1.1 on 2022-09-24 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='Address',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='user',
            name='Age',
            field=models.IntegerField(),
        ),
    ]
