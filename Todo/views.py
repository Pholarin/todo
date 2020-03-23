from django.shortcuts import render
from django.views.generic import ListView
from django.urls import reverse
from django.http import HttpResponseRedirect
from Todo.models import Task
from datetime import date,timedelta
from django.http import HttpResponse
from  django.contrib.auth.models  import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

# Create your views here.


class TodaytaskList(LoginRequiredMixin,ListView):
    template_name='Todo\\todaytask.html'
    model=Task

 

    def get_context_data(self,*args,**kwargs):
        context=super(TodaytaskList,self).get_context_data(*args,**kwargs)
        now=date.today()

        def get_queryset(self):
            return Task.objects.filter(user=self.request.user)

        context['alltask']=get_queryset(self)
        context['today']=now
        
        return context

@login_required
def marktask(request,id):
    queryset=Task.objects.get(pk=id)
    queryset.mark=True
    queryset.save()
    return HttpResponseRedirect(reverse('Todo:todaytask'))

@login_required
def addtask(request):
    
    if request.method=='POST':
       
        new_mytask= request.POST['mytask']
        new_descr=request.POST['descr']
        new_dateCreated=date.today()
        new_user=request.user

        newtask=Task(mytask=new_mytask,descr=new_descr,dateCreated=new_dateCreated,user=new_user)
        newtask.save()

        return HttpResponseRedirect(reverse('Todo:todaytask'))
