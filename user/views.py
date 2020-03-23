from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login,authenticate,logout
from django.contrib import messages

from .forms import SignUpForm
from django.urls  import reverse_lazy,reverse
from django.http import HttpResponseRedirect
from django.views.generic import CreateView
from user.models import TodoUser




class RegisterView(CreateView):
	model=TodoUser
	template_name='user//register.html'
	fields=('name','email','user')
	success_url=reverse_lazy('Todo:todaytask')



def createuser(request):
	form=SignUpForm(request.POST)
	if form.is_valid():
		form.save()
		username=form.cleaned_data.get('username')
		password=form.cleaned_data.get('password1')
		user=authenticate(username=username,password=password)
		login(request,user)
		return redirect('Todo:todaytask')
	else:
		form = SignUpForm
	return render(request,'user//register.html',{'form':form})


def login_user(request):
    
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
            
        user=authenticate(username=username,password=password)

        if user is not None:
            if user.is_active:
                login(request,user)



                return HttpResponseRedirect(reverse('Todo:todaytask'))
            else:
                return HttpResponse('User is not active')
        else:

            messages.error(request,"Invalid Username and Password combination")
            return HttpResponseRedirect(reverse('user:login'))
    return render(request,'user/login_form.html')



#logout
def logout_user(request):
        logout(request)
        return HttpResponseRedirect(reverse('user:login'))
