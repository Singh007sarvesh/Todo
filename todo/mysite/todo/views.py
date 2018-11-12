from django.shortcuts import render,  redirect, get_object_or_404
from django.http import HttpResponse, Http404
from rest_framework import generics
from rest_framework.views import APIView
from .models import Todo
from todo.serializers import TodoSerialize
import datetime
from datetime import timedelta


class TodoList(APIView):

	def get(self, request):
		todo_list = Todo.objects.order_by('due_date')
		todo = []
		todo_ = Todo.objects.all()
		for i in todo_:
			due_time = i.due_date
			if (due_time)   <= datetime.datetime.now().date() - timedelta(days=29):
				Todo.objects.filter(due_date=due_time).delete()
		for i in todo_list:
			due_time = i.due_date
			if (due_time) > datetime.datetime.now().date():
				concat = i.title + '   ' + i.description + '   ' + 'Pending'
				todo.append(concat)
			else:
				concat = i.title + ' ' + i.description + ' ' + 'Complete'
				todo.append(concat)
		return render(request, 'todo/home.html', {'todo': todo})	
	
	def post(self, request):
		todo_title = request.POST['todotitle']
		desc = request.POST['desc']
		date = request.POST['date']
		data = Todo(title = todo_title, description = desc, due_date = date)
		data.save()
		return redirect('addTodo')

class TodoSearch(APIView):
	def get(self, request):
		todo_search = request.GET['todo_search']
		todo_list = Todo.objects.filter(title = todo_search)
		if todo_search:
			return render(request, 'todo/home.html', {'todo_search_list': todo_list})

	def post(self,request):
		days = request.POST['week']
		if days == "today":
			return render(request, 'todo/home.html', {'today': Todo.objects.filter(due_date=datetime.datetime.now().date())})
		elif days == 'week':
			print(datetime.datetime.now().date())
			return render(request, 'todo/home.html', {'today': Todo.objects.filter(due_date=datetime.datetime.now().date())})
		elif days == 'next_week':
			print(datetime.datetime.now().date())
			return render(request, 'todo/home.html', {'today': Todo.objects.filter(due_date=datetime.datetime.now().date())})
		else:
			return render(request, 'todo/home.html', {'today': Todo.objects.filter(due_date__lte=datetime.datetime.now().date())})
