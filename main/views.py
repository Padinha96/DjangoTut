from django.shortcuts import render
from django.utils import translation
from .models import Tutorial

# Create your views here.
def homepage(request):
    translation.activate('en')
    return render(request=request,
                  template_name="main/home.html",
                  context={"tutorials": Tutorial.objects.all}
                  )
                