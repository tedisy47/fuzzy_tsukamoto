from django import forms 
from .models import Sekolah, Siswa

class Sekolahform(forms.ModelForm):
	class Meta:
		model = Sekolah
		fields = ['nama_sekolah', 'alamat_sekolah', 'biaya','lat']
	nama_sekolah = forms.CharField(
        label = "Nama Siswa",
        max_length = 80,
        required = True,
    )
	alamat_sekolah = forms.CharField(
		label='Alamat Sekolah',
        required = True,
        widget=forms.Textarea
        )
	biaya = forms.CharField(
		label='input biaya pertahun',
		required =  True,
		widget=forms.NumberInput
		)
	lat = forms.CharField(
		label='Latitude',
		required =  True,
		widget = forms.HiddenInput()
		)

class Siswaform(forms.ModelForm):
	class Meta:
		model = Siswa
		fields = ['nama_siswa', 'jenis_kelamin', 'tempat_lahir','tangal_lahir','user','gaji_pokok','asal_sekolah','alamat_siswa','lat']
	nama_siswa = forms.CharField(
        label = "Nama Siswa",
        max_length = 80,
        required = True,
    )
	jenis_kelamin = forms.ChoiceField(
		label='Jenis Kelamin',
        required = True,
        widget=forms.RadioSelect, choices=[('laki-laki', 'laki-laki'), ('perempuan', 'perempuan')]
        )
	tempat_lahir = forms.CharField(
		label='tempat lahir',
		required =  True,
		)
	tangal_lahir = forms.DateField(
		label='tanggal lahir',
		required =  True, 
		widget=forms.DateInput(     
        	attrs={'type': 'date'} 
    	)
		)
	gaji_pokok = forms.ChoiceField(
		label='Gaji Pokok Orang Tua',
		required =  True,
		widget=forms.RadioSelect, choices=[('<=2000.000', '<=2000.000'), ('>2000.000', '>2000.000')]
		)
	alamat_siswa = forms.CharField(
		label='Alamat',
		required =  True,
		widget=forms.Textarea
		)
	asal_sekolah = forms.CharField(
		label='asal Sekolah',
		required =  True,
		)
	user = forms.CharField(
		label='Latitude',
		required =  True,
		widget = forms.HiddenInput(

        	# initial={'Useer': use}	
			)
		)
	lat = forms.CharField(
		label='Latitude',
		required =  True,
		widget = forms.HiddenInput()
		)