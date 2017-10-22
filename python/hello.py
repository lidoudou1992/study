# std1 = {"name": "lidoudou", "score": 100}
# std2 = {"name": "jasgfb", "score": 0}

# def  ptint_score(std):
# 	print("%s: %s" % (std["name"], std["score"]))

class Student(object):
	"""docstring for Student"""
	def __init__(self, name, score):
		self.name = name
		self.score = score
	
	def print_score(self):
		print("%s: %s" % (self.name, self.score))

	def get_grade(self):
		if self.score >= 90:
			return "A"
		elif self.score >= 60:
			return "B"
		else:
			return "C"


# appel = Student("dsfaf", 90)
# banana = Student("asdasd", 10000)
# appel.print_score()
# banana.print_score()