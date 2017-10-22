# -*- coding:utf-8 -*-
import hello

def test(score):
	bart = hello.Student("lifoufouerwr", 78)
	# print (bart.name)
	bart.score = set_grade(score)
	# bart.print_score()
	if bart.get_grade() == "A":
		print ("成绩很是优秀")
	else:
		print ("垃圾")


def set_grade(reward):
	return reward

# test()
