from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout


def register(request):

    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/jobs/')

    else:
        form = UserCreationForm()

    return render(request, 'accounts/register.html', {'form': form})

def user_login(request):

    error = ''

    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:

            login(request, user)

            next_url = request.GET.get('next')

            if next_url:
                return redirect(next_url)

            return redirect('/jobs/')

        else:
            error = 'Invalid username or password'

    return render(
        request,
        'accounts/login.html',
        {'error': error}
    )

def user_logout(request):

    logout(request)

    return redirect('/accounts/login/')