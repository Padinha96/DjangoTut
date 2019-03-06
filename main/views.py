from django.shortcuts import render
from django.utils import translation
from django.contrib.auth.forms import UserCreationForm
from .models import Tutorial

# Create your views here.
def homepage(request):
    translation.activate('en')
    return render(request=request,
                  template_name="main/home.html",
                  context={"tutorials": Tutorial.objects.all}
                  )


def register(request):
    form = UserCreationForm
    return render(request,
                  "main/register.html",
                  context={"form":form})
