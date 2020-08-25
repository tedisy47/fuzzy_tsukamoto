from django.db import models

# Create your models here.
class Klaster(models.Model):
	a = models.FloatField()
	b = models.FloatField()
	index = models.IntegerField()

class Dataset(models.Model):
	"""docstring for dataset"""
	nama = models.CharField(max_length=225)
	x = models.FloatField()
	y = models.FloatField()

class Proses(models.Model):
	"""docstring for dataset"""
	dataset_id = models.IntegerField()
	hasil = models.FloatField()
	index_kluster = models.CharField(max_length=225)
	kluster = models.IntegerField()


class hasil(models.Model):
	"""docstring for dataset"""
	dataset_id = models.IntegerField()
	kluster = models.IntegerField()