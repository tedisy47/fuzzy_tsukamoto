# Generated by Django 3.0.7 on 2020-08-26 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fuzy', '0005_proses'),
    ]

    operations = [
        migrations.AddField(
            model_name='proses',
            name='bobot',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]