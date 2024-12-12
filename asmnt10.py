#else !!
subject1 =int(input("enter marks for subject1:"))
subject2 =int(input("enter marks for subject2:"))
subject3 =int(input("enter marks for subject3:"))
subject4 =int(input("enter marks for subject4:"))

totalmarks = subject1 + subject2 + subject3 + subject4
print(totalmarks)
if totalmarks >=90:
          print("your grade A+")
elif totalmarks >=80:
          print("your grade A")
elif totalmarks >=70:
          print("your grade B")
elif totalmarks >=60:
          print("your grade C")
elif totalmarks >=50:
          print("your grade D")
          