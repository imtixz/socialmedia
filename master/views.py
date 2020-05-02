from django.shortcuts import render

def home(request):
	return render(request, 'master/home.html')

def about(request):
	return render(request, 'master/about.html')

def help(request):
	return render(request, 'master/help.html')

def profile(request):
	return render(request, 'master/profile.html')