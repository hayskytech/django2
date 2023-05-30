from django.http import HttpResponse
from django.shortcuts import render
import sqlite3

def about(r):
	return HttpResponse("<h1>About us</h1>")

def home(r):
	con = sqlite3.connect("db.sqlite3")
	cur = con.cursor()
	res = cur.execute("SELECT name from sqlite_master")
	tables = res.fetchall()

	if ('student',) not in tables:
		cur.execute("CREATE TABLE student (student,father,phone)")
		con.commit()
	
	s = r.GET.get("student")	
	father = r.GET.get("father")	
	phone = r.GET.get("phone")	
	data = (s,father,phone)

	if s:
		cur.execute("INSERT INTO student VALUES (?,?,?)" , data)
		con.commit()

	if r.GET.get("delete"):
		sd = r.GET.get("dstudent")
		sd_tuple = (sd,)
		cur.execute("DELETE FROM student WHERE student=?" , sd_tuple)
		con.commit()
	
	res = cur.execute("SELECT * FROM student")
	students = res.fetchall()

	data = {
		"students" : students
	}



	return render(r,"home.html", data)
