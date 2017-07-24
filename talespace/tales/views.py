from django.shortcuts import render
from django.http import HttpResponse

from django.contrib.auth.models import User
from .models import Author, Tale
from .forms import UserForm


def index(request):
    tales = Tale.objects.all()
    context = {
        'tales': tales,
    }
    return render(request, 'tales/index.html', context)

def tales_list(request):
    tales = Tale.objects.all()
    context = {
        'tales': tales,
    }
    return render(request, 'tales/tales_list.html', context)

def tale_details(request, tale_id):
    tale = Tale.objects.get(id=int(tale_id))
    context = {
        'tale': tale,
    }
    return render(request, 'tales/tale_details.html', context)

def user_add(request):
    form = UserForm(request.POST)
    if form.is_valid():
        try:
            user = User()
            user.username = form.cleaned_data['email']
            user.first_name = form.cleaned_data['first_name']
            user.last_name = form.cleaned_data['last_name']
            user.email = form.cleaned_data['email']
            user.password = form.cleaned_data['password']
            user.save()
            request.user = user
            context = {
                'user': user,
            }
            return render(request, 'tales/sign_up.html', context)
        except:
            return HttpResponse("Submit form failed! :(")
    else:
        return HttpResponse("Submit form failed! :(")

def user_profile(request, user_id):
    if request.user.is_authenticated():
        context = {
            'user': request.user,
        }
        return render(request, 'tales/user_profile.html', context)
    else:
        return HttpResponse("User is not logged in or does not match attempted Profile ID --> %s!" % user_id)
    