from django import forms
from .models import Task
from datetime import datetime

today_day = datetime.today().strftime('%Y-%m-%d')

class TaskForm(forms.ModelForm):

	class Meta:
		model = Task
		fields = ['task', 'deadline']
		widgets = {
			"task": forms.TextInput(attrs={"class": "task-add1", 'placeholder':'ADD TASK', 'autocomplete':"off"}),
			"deadline": forms.TimeInput(attrs={"class": "task-add2", 'type':'date', 'id':'txtDate', 'value':f"{today_day}"}),
		}
	
class TaskDoneForm(forms.ModelForm):

	class Meta:
		model = Task
		fields = ['done']