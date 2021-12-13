from django.urls import path
from . import views


urlpatterns = [
	path('', views.TaskList.as_view(), name='main'),
	path('<int:pk>/delete/', views.DeleteTask.as_view(), name='delete'),
	path('done/<int:pk>', views.FormDone.as_view(), name='done'),
	path('add/', views.TaskAdd.as_view(), name='add'),

]