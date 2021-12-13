from django import template
from ..models import Task


register = template.Library()

@register.simple_tag()
def total_tasks():
	return Task.objects.count()


@register.simple_tag()
def done_tasks():
	return Task.objects.filter(done=True).count()

