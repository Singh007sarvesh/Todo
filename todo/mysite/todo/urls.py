from django.conf.urls import url
from todo import views
from django.urls import path
urlpatterns = [
	# path('', views.TodoList.as_view()),
	path('?', views.TodoSearch.as_view(), name='search'),
	path('', views.TodoList.as_view(), name='addTodo'),
	
]