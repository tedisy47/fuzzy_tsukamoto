# Generated by Django 3.0.7 on 2020-08-25 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fuzy', '0003_siswa'),
    ]

    operations = [
        migrations.AlterField(
            model_name='siswa',
            name='gaji_pokok',
            field=models.CharField(max_length=225),
        ),
    ]
