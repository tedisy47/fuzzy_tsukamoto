from django.shortcuts import render

# Create your views here.
def index(request):
	return render(request,'login.html')
def login(request):
	if requests.method == 'POST':
		# print(requests)
		user = authenticate(username=requests.POST['username'], password=requests.POST['password'])
		if user is not None:
			if user.is_active is True:
				auth_login(requests, user)
				messages.add_message(requests, messages.INFO, 'Selamat datang.')
				return redirect('/home/')
				# return HttpResponse('ok')
	else:
		return redirect('/fuzzy/')
def register(request):
	return render(request,'register.html')