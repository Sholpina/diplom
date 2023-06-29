from django.db import IntegrityError
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login


# Create your views here.
def signupuser(request):
        if request.method == 'GET':
                return render(request, 'lawersagenda\signupuser.html', {'form': UserCreationForm()})
        else:
                # создание нового пользователя
                # User.objects.create_user(request.POST['username'], password=)
                if request.POST['password1'] == request.POST['password2']:
                        try:
                                user = User.objects.create_user(request.POST['username'],
                                                                password=request.POST['password1'])
                                login(request, user)
                                user.save()
                                return redirect('lawersagenda:currentagenda')

                        except IntegrityError:
                                return render(request, 'lawersagenda/signupuser.html',
                                              {'form': UserCreationForm(),
                                               'error': 'That username has already been taken. Please choise a new username '})
                else:
                        # Tell the user password didn't match
                        return render(request, 'lawersagenda/signupuser.html',
                                      {'form': UserCreationForm(), 'error': 'Password did not match'})


def currentagenda(request):
        return render(request, 'lawersagenda/currentagenda.html')
