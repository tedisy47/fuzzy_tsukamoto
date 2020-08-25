from django import forms 
from .models import Dataset 

class Datasetform(forms.ModelForm):
	class Meta:
		model = Dataset
		fields = ['nama', 'x', 'y',]
	nama = forms.CharField(
        label = "Nama Siswa",
        max_length = 80,
        required = True,
    )
	x = forms.FloatField(label='Rata-rata Nilai Pengetahuan',
        required = True,)
	y = forms.FloatField(label='Rata-rata Nilai Keterampilan',
        required = True,)