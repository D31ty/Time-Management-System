from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm

from django.contrib import messages
from django.core.mail import EmailMessage

from django_email_verification import send_email

from .forms import CreateUserForm

from django.views.decorators.cache import cache_control
from .forms import SignupForm
from .models import UserAccount

# Create your views here.


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def verification(request):
	user = request.user
	return render(request, 'register/verification.html')


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def registerPage(request):
	'''if request.user.is_authenticated:
		return redirect('tasks:home')                             
	else:
		if request.method == 'POST':
			form = CreateUserForm(request.POST)
			if form.is_valid():
				user = form.save()
				user.is_active = False
				send_email(user)
				return redirect("verification")
				#login(request, user)
				#return redirect('tasks:home')
		
		else:
			form = CreateUserForm()


		return render(request, 'register/register.html', {'form': form})'''

	if request.method == "POST":
		form = SignupForm(request.POST)
		phone = request.POST['phone']
		if form.is_valid():
			user = UserAccount.objects.create_user(
						username = request.POST['username'],
						email=request.POST['email'],
						phone = phone,
						password=request.POST['password1'], 
						)
			user.save()
			user.is_active = True
			send_email(user)
			return redirect("verification")

		else:
			return render(request, 'register/register.html', {
					'form': form
				})
		return redirect('tasks:home')

	else:
		form = SignupForm()

	return render(request, 'register/register.html', {
        'form': form
    })


def loginPage(request):
	'''if request.user.is_authenticated:
			return redirect('tasks:home')
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password =request.POST.get('password')

			user = authenticate(request, username=username, password=password)
			if user is not None:
				login(request, user)
				return redirect('tasks:home')
			else:
				messages.info(request, 'Username OR password is incorrect')

		return render(request, 'register/login.html')'''

	'''if request.user.is_authenticated:
			return redirect('tasks:home')
	else:
		if request.method == 'POST':
			user = authenticate(request, username=request.POST["username"], password=request.POST["password"])
			form = AuthenticationForm(request.POST)
			if user is not None:
				login(request, user)
			else:
				return render(request, 'register/login.html', {'form': form, 'error': "Invalid credentials"})
			return redirect('tasks:home')

		else:
			form = AuthenticationForm()
			return render(request, "register/login.html", {'form': form})'''
	
	if request.method == 'POST':
		user = authenticate(request, username=request.POST["username"], password=request.POST["password"])
		form = AuthenticationForm(request.POST)
		if user is not None:
			login(request, user)
		else:
			return render(request, 'register/login.html', {
                'form': form,
                'error': "Invalid credentials"
            })
		return redirect('tasks:home')
	else:
		form = AuthenticationForm()
		return render(request, "register/login.html", {
            'form': form
        })

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required
def logoutUser(request):
	logout(request)
	request.session.flush()
	return redirect('login')
   