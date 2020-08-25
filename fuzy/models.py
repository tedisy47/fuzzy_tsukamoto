from django.db import models

# Create your models here.
class Sekolah(models.Model):
	nama_sekolah = models.CharField(max_length=225)
	alamat_sekolah = models.TextField()
	biaya = models.IntegerField()
	lat = models.CharField(max_length=225)
class Siswa(models.Model):
	nama_siswa = models.CharField(max_length=225)
	jenis_kelamin = models.CharField(max_length=225)
	tempat_lahir = models.CharField(max_length=225)
	tangal_lahir = models.DateField()
	user = models.CharField(max_length=225)
	gaji_pokok = models.IntegerField()
	asal_sekola = models.CharField(max_length=225)
	alamat_siswa = models.TextField()
	lat = models.CharField(max_length=225)