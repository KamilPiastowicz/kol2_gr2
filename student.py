class student(object):

 def __init__(self,name, surname):
  self.student_id = 0
  self.name = name
  self.surname = surname
  self.attended = 0
  self.obligated = 0
  self.grades = []

 def __str__(self):
  print self.name + " " + self.surname + " " + avg_grade + " " + get_attendance

 def check_attendance(self,is_on_class):
  self.obligated += 1
  if is_on_class:
   self.attended += 1

 def add_grade(self,grade):
  grades.extend(grade)

 def avg_grade(self):
  return sum(grades)/len(grades)

 def set_id(self,stud_id):
  self.student_id = stud_id

 def get_attendance(self):
  return self.attended/self.obligated

if __name__ = "__main__":
