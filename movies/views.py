from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import MovieForm
from django.contrib.auth.forms import UserChangeForm

def dashboard(request):
    return render(request, 'movies/dashboard.html')


def add_movie(request):
    if request.method == 'POST':
        form = MovieForm(request.POST)

        if form.is_valid():
            movie = form.save(commit=False)
            movie.user = request.user
            movie.save()
            return redirect('dashboard')
    else:
        form = MovieForm()

    return render(request, 'movies/add_movie.html', {'form': form})



def registration(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()

    return render(request, 'registration/register.html', {'form': form})