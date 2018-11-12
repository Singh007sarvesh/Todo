from django.test import TestCase
from todo.models import Todo
from rest_framework.test import APIClient
from rest_framework.authtoken.models import Token
# Create your tests here.

class TodoAPITest(TestCase):
	def setUp(self):
		todo = [
            {
            	"title": "anurag",
                "description": "anurag@nitc",
                "due_date": "11/05/2018"
            },
            {
                "title": "anurag1",
                "description": "anurag@nitc1",
                "due_date": "11/25/2018"
            },
        ]

	def test_todo_invalid(self):
		client = APIClient()
		response = client.get('todo/')
		self.assertEqual(response.status_code, 404)
		response = client.post('todo/')
		self.assertEqual(response.status_code, 404)
	
	def test_todolist(self):
		client = APIClient()
		response = client.get('/todos/',{'title': 'anurag', 'description': 'anurag@nitc', 'due_date': '11/05/2018'})
		self.assertEqual(response.status_code, 200)