# Generated by Django 3.0.7 on 2020-08-10 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kmeans', '0007_auto_20200807_1406'),
    ]

    operations = [
        migrations.AlterField(
            model_name='klaster',
            name='a',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='klaster',
            name='b',
            field=models.FloatField(),
        ),
    ]
