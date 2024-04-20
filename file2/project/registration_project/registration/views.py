from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .forms import RegistrationForm

def register(request):
    template = loader.get_template("registration/index.html")
    if request.method == 'POST':
        form = RegistrationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = RegistrationForm()
    return render(request, "polls/index.html", {'form': form})

def success(request):
    return render(request, 'registration/success.html')

