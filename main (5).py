class student:

  def__init__(self, name, roll_number, cgpa) :
    self.name=name
    self. roll_number=roll_number
    self. cgpa=cgpa


def sort_students(student_list) :

  sorted_student=sorted(stident_list, key=lambda student: student. cgpa, reverse=true)


   return sorted_students



students=[
  student("Hari", "A123",7.8),
student(" venu","A124",8.9) 
student("meena",A125",5.1)
student("kaviya", "A126", 9.9) 
]
sorted_student=sort_students(students)
for student in sorted_students:
  print(" Name: {}, roll number:{}, CGPA:{},. format(student.name, student. roll_number, student. ch pa)) "
  
