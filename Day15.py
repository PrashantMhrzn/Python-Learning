# OOP
class StudentForm:
	firstname = 'ram'
	lastname = 'bahadur'
	age = 10
	
	def get_info(self):
		print(f'Firstname: {self.firstname}')
	
	def set_into(self, firstname):
		self.firstname = firstname
		self.get_info()
		
# s1 = StudentForm()
# print(s1.age)
# s1.age = 30
# print(s1.age)

# s2 = StudentForm()
# s2.set_info('Gopal')