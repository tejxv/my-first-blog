from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm

def register(request):
	if request.method =='POST':
		print('method is post')
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			print('done')
			form.save()
			username = form.cleaned_data.get('username')
			messages.success(request, f'Account Successfully Created, { username }!')
			return redirect('/')
		else:
		    messages.warning(request, f'Please enter valid credentials!')	
	form = UserRegisterForm()
	print('falled back')
	return render(request, 'users/register.html', {'form': form})

