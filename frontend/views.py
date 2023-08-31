from django.shortcuts import render, redirect

def index(request, *args, **kwargs):
  return render(request, 'index.html')

def redirect_to_home(request, *args, **kwargs):
  return redirect('/')
