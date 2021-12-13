from django.db import models
from django.urls import reverse
from datetime import date


class Task(models.Model):
	task = models.CharField(max_length=50)
	created = models.DateField(auto_now_add=True)
	deadline = models.DateField(null=True, blank=True)
	done = models.BooleanField(default=False)
	

	def __str__(self):
		return self.task

	def get_absolute_url(self):
		return reverse('main')

	def days_remain(self):
		days = self.deadline - date.today()
		if self.created == self.deadline:
			return False
		else:
			return days.days

	def deadline_check(self):
		if self.created == self.deadline:
			return False
		else:
			return True

		
