class Student:
     count_of_Student = 0
     def __init__(self, name=None, height=160):
         self.name = name
         self.height = height
         Student.count_of_Student += 1
         print('привет я появился')

     def grow(self, height=1):
         self.height += height

     def __str__(self):
        return f'я {self,name}, мой рост {self.height} см'

Serg = Student(height=180)
print(Serg.height)

Artur = Student(name='Artur', height=165)
print(Artur.height)
print('Artur.count_of_Student')
print('Serg.count_of_Student')
print('Student.count_of_Student')
Artur.grow(10)
print(Artur.height)


