# Generated by Django 3.0.7 on 2020-08-11 17:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kmeans', '0010_auto_20200810_1634'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='proses',
            name='index',
        ),
    ]