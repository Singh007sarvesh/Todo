from django.test import TestCase
from todo.models import Todo
from rest_framework.test import APIClient
import datetime

class TodoListAPITest(TestCase):
	def setUp(self):
		todo = Todo.objects.create(title="Diwali", description="user", due_date="2018-11-13")
	def test_todo_invalid(self):
		client = APIClient()
		response = client.get('todo/')
		self.assertEqual(response.status_code, 404)
		response = client.post('todo/')
		self.assertEqual(response.status_code, 404)
	
	def test_todolist(self):
		client = APIClient()
		data = Todo(title = 'abc', description = 'xyz', due_date = '2018-11-13')
		# response = client.post('/api/todos/', data)
		# self.assertEquals(response.status_code,201)
		response = client.get('/api/todos/')
		self.assertEquals(response.status_code, 200)


class TodoSearchAPITest(TestCase):

	def setUp(self):
		todo = Todo.objects.create(title="Diwali", description="user", due_date="2018-11-13")

	def test_todo_search_invalid(self):
		client = APIClient()
		response = client.get('api/todos/?')
		self.assertEqual(response.status_code, 404)
		response = client.post('api/todos/?')
		self.assertEqual(response.status_code, 404)

	def test_todo_search(self):
		client = APIClient()
		todo_list = Todo.objects.filter(title = "Diwali")
		if todo_list:
			response = client.get('/api/todos/?/')
			self.assertEquals(response.status_code,200)
		days = 'today'
		if days == "today":
			data = Todo.objects.filter(due_date='2018-11-13')
			response = client.get('/api/todos/?/', data)
			self.assertEquals(response.status_code,200)