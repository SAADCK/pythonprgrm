
array_input=input("enter the numbers:")
num=int(input("enter a number:"))
def fun1():
          if num%2==0:
                    print("number is even")
          else:
                    print("number is odd")

def fun2():
       for x in range(1, 11):
          print(f"{num}x{x}={num*x}")   
          
def fun3():
          
          array= list(map(int, array_input.split()))
          
          
          if num in array:
                    print(f"{num} is found in the array.")
          else:
                    print(f"{num} is not found in the array.")
                    

          
          
fun1()
fun2()
fun3()