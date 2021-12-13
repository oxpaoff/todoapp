from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.base import View
from .models import Task
from .forms import TaskForm, TaskDoneForm
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy



class TaskList(ListView):
	model = Task
	template_name = 'main.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['tasks'] = Task.objects.all()
		context['done_form'] = TaskDoneForm
		context['form'] = TaskForm
		if Task.objects.count() > 0:
			if Task.objects.count() == Task.objects.filter(done=True).count():
				context['done_all'] = True
		else:
			context['done_all'] = False
		return context




class FormDone(View):
	def post(self, request, pk):
		done_form = TaskDoneForm(request.POST)
		if request.method == 'POST':
			if done_form.is_valid():
				task = Task.objects.get(id=pk)
				if task.done==True:
					task.done=False
				else:
					task.done=True
				task.save()

				return redirect('main')
			else:
				done_form = TaskDoneForm()

class TaskAdd(View):
	def post(self, request):
		form = TaskForm(request.POST)
		if request.method == 'POST':
			if form.is_valid():
				form.save()

				return redirect('main')
			else:
				form = TaskForm()				

class DeleteTask(DeleteView):
	model = Task
	template_name = 'delete.html'
	success_url = reverse_lazy('main')


