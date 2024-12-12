class student:
          def __init__(self,name,age):
                    self.__name = name
                    self.__age  = age
          def get_name(self):
                    return self.__name
          def get_age(self):
                    return self.__age
          def set_age(self,age):
                    if age > 0:
                              self.__age = age
                    else:
                              print("age must be a positive integer.")
student = student("alice",20)
print(f"student name: {student.get_name()}")
print(f"student name: {student.get_age()}")
student.set_age(21)
print(f"Updated Age:{student.get_age()}")                              
          