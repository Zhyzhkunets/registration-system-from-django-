from django.shortcuts import render
from django.http import HttpResponseRedirect

# my models
from models import CustomUser, Post

# my forms
from forms import CustomUserForm

# security
from django.views.decorators.debug import sensitive_post_parameters
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect


# django auth form 
from django.contrib.auth.forms import AuthenticationForm

# django auth "tools"
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required

def home_view(request):
    posts = Post.objects.order_by('-id')
    return render(request, 'home.html', {'posts':posts})

@sensitive_post_parameters()
@csrf_protect
@never_cache
def login(request): # I think, 'login_view' is better and correct 

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            auth_login(request, form.get_user())

            return HttpResponseRedirect('/loggedin/')
    else:
        form = AuthenticationForm(request)

    return render(request, 'login.html', {'form':form})

def logout(request):
	auth_logout(request)
	return render(request, 'logout.html')

def loggedin(request):
	
	context  = {
	    'full_name':request.user.username
	}

	return render(request, 'loggedin.html', context)

def registrate_view(request):
    
    if request.method == 'POST':
    	form = CustomUserForm(request.POST)

        if form.is_valid():
            form.save()

            return HttpResponseRedirect('/loggedin/') # redirect must be other
    else:
        form = CustomUserForm()

    return render(request, 'registrate.html', {'form':form})




