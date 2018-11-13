from django.test import TestCase
from todo.models import Todo
from rest_framework.test import APIClient


class TodoListAPITest(TestCase):
	def setUp(self):
		self.todo = [
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
		response = client.get('/todos/')
		self.assertEqual(response.status_code, 200)
		todo_title = 'Diwali'
		desc = 'abc'
		date = '11/13/2018'
		data = Todo(title = todo_title, description = desc, due_date = date)
		response = client.post('/todos/', {'title':todo_title,'description': desc,'due_date':date})
		self.assertEquals(response.status_code,201)


# class TodoSearchAPITest(TestCase):

# 	def setUp(self):
# 		self.todo = [
#             {
#             	"title": "anurag",
#                 "description": "anurag@nitc",
#                 "due_date": "11/05/2018"
#             },
#             {
#                 "title": "anurag1",
#                 "description": "anurag@nitc1",
#                 "due_date": "11/25/2018"
#             },
#         ]

# 	def test_todo_search(self):
# 		client = APIClient()
# 		import pdb;pdb.set_trace()
# 		todo_list = Todo.objects.filter(title = "Diwali")
# 		if todo_list:
# 			print("hello---->")
# 			response = client.get('/todos/?/')
# 			self.assertEquals(response.status_code,200)
# 		# if todo_search:
# 		# 	return render(
# 		# 	request, 'todo/home.html', {'todo_search_list': todo_list})