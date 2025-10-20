from django.shortcuts import render
from .forms import RegistartionForm


# Create your views here.
def register(request):
    form= RegistartionForm()
    context = {'form':form}
    return render(request, 'accounts/register.html', context)

def login(request):
    return render(request, 'accounts/login.html')

def logout(request):
   pass