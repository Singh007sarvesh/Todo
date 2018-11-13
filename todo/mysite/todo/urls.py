from django.conf.urls import url
from todo import views
from django.urls import path
urlpatterns = [
	# path('', views.TodoList.as_view()),
	path('todos/?', views.TodoSearch.as_view(), name='search'),
	path('todos/', views.TodoList.as_view(), name='addTodo'),
	
]