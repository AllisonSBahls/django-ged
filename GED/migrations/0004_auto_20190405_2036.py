# Generated by Django 2.1.7 on 2019-04-06 00:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GED', '0003_auto_20190405_2013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anexo',
            name='url',
            field=models.FileField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='documento',
            name='url',
            field=models.FileField(upload_to=''),
        ),
    ]
