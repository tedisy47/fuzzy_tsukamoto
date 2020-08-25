from django import forms 
from .models import Sekolah 

class Sekolahform(forms.ModelForm):
	class Meta:
		model = Sekolah
		fields = ['nama_sekolah', 'alamat_sekolah', 'biaya','lat','lng']
	nama_sekolah = forms.CharField(
        label = "Nama Siswa",
        max_length = 80,
        required = True,
    )
	alamat_sekolah = forms.TextField(
		label='Rata-rata Nilai Pengetahuan',
        required = True,
        )
	biaya = forms.IntergerField(
		label='input biaya pertahun',
		required =  True
		)
	lat = forms.CharField(
		label='Latitude',
		required =  True,
		readonly = True
		)
	lng = forms.CharField(
		label='lng',
		required =  True,
		readonly = True
		)