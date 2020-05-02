from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Profile
from django.http import Http404
from django.core.exceptions import PermissionDenied
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm

def register(request):
	#When receiving the form
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)

		#If the form is valid, create an account and redirect user to login page
		if form.is_valid():
			form.save()
			messages.success(request, f"Your account has been created. You can now log in.")
			return redirect('login')


	#When sending the form
	else:
		form = UserRegisterForm()

	return render(request, 'accounts/register.html', {'form':form})


@login_required()
def profile(request, given_username):
	try: 
		getUser = User.objects.get(username=given_username)
		getProfile = Profile.objects.get(user=getUser)

		if request.user.username == given_username:
			context = {'username':getUser.username, 'email':getUser.email,
			'fullname':getProfile.fullname, 'bio':getProfile.bio, 'owner':True}

		else:
			context = {'username':getUser.username, 'email':getUser.email, 
			'fullname':getProfile.fullname, 'bio':getProfile.bio, 'owner':False}

		return render(request, 'accounts/profile.html', context)

	except e as Exception:
		raise Http404(e)

@login_required()
def profile_edit(request, given_username):

	if request.user.username == given_username:
		context = {'username':given_username, 'owner':True}

		if request.method == 'POST':
			u_form = UserUpdateForm(request.POST, instance=request.user)
			p_form = ProfileUpdateForm(request.POST, instance=request.user.profile)

			if u_form.is_valid() and p_form.is_valid():
				u_form.save()
				p_form.save()
				messages.success(request, f"Your account has been updated.")
				return redirect('profile', given_username = request.user.username)
		else:
			u_form = UserUpdateForm(instance=request.user)
			p_form = ProfileUpdateForm(instance=request.user.profile)

		context = {
			'u_form':u_form,
			'p_form':p_form
		}

		return render(request, 'accounts/profile_edit.html', context)


	else:
		raise PermissionDenied
