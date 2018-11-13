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
			return render(
			request, 'todo/home.html', {'todo_search_list': todo_list})

	def post(self,request):
		days = request.POST['week']
		if days == "today":
			return render(
			request, 'todo/home.html', {'today': Todo.objects.filter(
			due_date=datetime.datetime.now().date())})
		elif days == 'week':
			day = 0
			diff_day = 0
			cur_date = str(datetime.datetime.now().date())
			days_ = datetime.datetime.strptime(cur_date, '%Y-%m-%d').strftime('%A')
			if days_ == 'Monday':
				day = 7
				diff_day = 0
			elif days_ == 'Tuesday':
				day = 6
				diff_day = 1
			elif days_ == 'Wednesday':
				day = 5
				diff_day = 2
			elif days_ == 'Thursday':
				day = 4
				diff_day = 3
			
			elif days_ == 'Friday':
				day = 3
				diff_day = 4
			elif days_ == 'Saturday':
				day = 2
				diff_day = 5
			elif days_ == 'Sunday':
				day = 1
				diff_day = 6
			total_days_gt = datetime.datetime.now().date() + timedelta(days=day)
			total_days_ls = datetime.datetime.now().date() - timedelta(days=diff_day)
			return render(
			request, 'todo/home.html', {'today': Todo.objects.filter(
			due_date__lte=total_days_gt,due_date__gte=total_days_ls)})
		elif days == 'next_week':
			day = 0
			cur_date = str(datetime.datetime.now().date())
			days_ = datetime.datetime.strptime(cur_date, '%Y-%m-%d').strftime('%A')
			if days_ == 'Monday':
				day = 7
			elif days_ == 'Tuesday':
				day = 6
			elif days_ == 'Wednesday':
				day = 5
			elif days_ == 'Thursday':
				day = 4
			
			elif days_ == 'Friday':
				day = 3
			elif days_ == 'Saturday':
				day = 2
			elif days_ == 'Sunday':
				day = 1
			total_days_gt = datetime.datetime.now().date() + timedelta(days=day)
			return render(
			request, 'todo/home.html', {'today': Todo.objects.filter(
			due_date__gte=total_days_gt)})
		else:
			return render(
			request, 'todo/home.html', {'today': Todo.objects.filter(
			due_date__lte=datetime.datetime.now().date())})

