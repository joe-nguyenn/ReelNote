from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import MovieForm


def dashboard(request):
    return render(request, 'movies/dashboard.html')

@login_required
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

    