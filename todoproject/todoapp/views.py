from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy

from .models import Task
from .forms import TodoForms
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView,DeleteView

# Create your views here.

class Tasklistview(ListView):
    model = Task
    template_name = 'home.html'
    context_object_name = 'task1'

class TaskDetailview(DetailView):
    model = Task
    template_name = 'details.html'
    context_object_name = 'task1'

class TaskDeleteview(DeleteView):
    model = Task
    template_name = 'delete.html'
    success_url = reverse_lazy('cbvhome')

class TaskUpdateview(UpdateView):
    model = Task
    template_name = 'edit.html'
    context_object_name = 'task1'
    fields = ('name','priority','date')

    def get_success_url(self):
        return reverse_lazy('cbvdetail',kwargs={'pk':self.object.id})
def add(request):
    if request.method=='POST':
        name=request.POST.get('name')
        priority=request.POST.get('priority')
        date=request.POST.get('date')
        task=Task(name=name,priority=priority,date=date)
        task.save()
    # task1=Task.objects.all()
        return render(request,'home.html',{'task':task})
# def home(request):

# def delete(request,id):
#     task = Task.objects.get(id=id)
#     if request.method=='POST':
#         task.delete()
#         return redirect('/')
#     return render(request,'delete.html')
#
# def update(request,id):
#     task=Task.objects.get(id=id)
#     f=TodoForms(request.POST or None, instance=task)
#     if f.is_valid():
#         f.save()
#         return redirect('/')
#     return render(request,'edit.html',{'f':f,'task':task})
