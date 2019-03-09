from django.shortcuts import render, redirect
#from django.http import HttpResponse
from django.utils import translation
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from .models import Tutorial, TutorialCategory, TutorialSeries
from .forms import NewUserForm

def single_slugger(request, single_slug):
    categories = [c.slug for c in TutorialCategory.objects.all()]
    if single_slug in categories:
        matching_series = TutorialSeries.objects.filter(category__slug=single_slug)
        series_url = {}
        for match in matching_series.all():
            part_one = Tutorial.objects.filter(series__series=match.series).earliest("published")
            series_url[match] = part_one.slug
        return render(request,
                      "main/category.html",
                      {"part_ones": series_url})
    tutorials = [c.slug for c in Tutorial.objects.all()]
    if single_slug in tutorials:
        tut = Tutorial.objects.get(slug=single_slug)
        serie_tuts = Tutorial.objects.filter(series__series=tut.series).order_by("published")
        tut_idx = list(serie_tuts).index(tut)
        return render(request,
                      "main/tutorial.html",
                      {"tutorial":tut, "sidebar":serie_tuts, "index":tut_idx})

# Create your views here.
def homepage(request):
    translation.activate('en')
    return render(request=request,
                  template_name="main/categories.html",
                  context={"categories": TutorialCategory.objects.all}
                  )


def register(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"User {username} created succesfully")
            login(request, user)
            messages.info(request, f"You are now logged in as {username}")
            return redirect("main:homepage")
        else:
            for msg in form.error_messages:
                messages.error(request, f"{msg}: {form.error_messages[msg]}")

    form = NewUserForm
    return render(request,
                  "main/register.html",
                  context={"form":form})

def logout_request(request):
    logout(request)
    messages.info(request, f"You have logged out")
    return redirect("main:homepage")


def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}")
                return redirect("main:homepage")
            else:
                messages.error(request, f"Invalid username or password")
        else:
            messages.error(request, f"Invalid username or password")
    form = AuthenticationForm()
    return render(request,
                  "main/login.html",
                  context={"form":form})
