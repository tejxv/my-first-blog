from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm

def register(request):
	if request.method =='POST':
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			print('done')
			form.save(commit=False)
			username = form.cleaned_data.get('username')
			messages.success(request, f'user { username } successfully created! now you can login using the login button above')
			return redirect('/')
		else:
		    messages.warning(request, f'Please enter valid details!')	
	form = UserRegisterForm()
	print('falled back')
	return render(request, 'users/register.html', {'form': form})

