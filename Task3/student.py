from account import Account


class Student(Account):
	"""docstring for Student"""
	def __init__(self, username, password, type):
		super(Student, self).__init__()
		self.username = username
		self.password = password
		self.type = type
		