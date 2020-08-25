# Generated by Django 3.0.7 on 2020-08-07 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kmeans', '0006_auto_20200807_1406'),
    ]

    operations = [
        migrations.CreateModel(
            name='hasil',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dataset_id', models.IntegerField()),
                ('kluster', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='proses',
            name='index',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='proses',
            name='x',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='proses',
            name='y',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
    ]
