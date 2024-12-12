def fun1(num):
          if num%2==0:
                    print("number is even")
          else:
                    print("number is odd")
                    
def fun2(num):
          for x in range(1, 11):
                    print(f"{num}x{x}={num*x}") 
def fun3(num):
          array_input=[1,2,3,4,5]
          if num in array_input:
                    print(f"{num} is found in the array.")
          else:
                    print(f"{num} is not found in the array.")
fun1(5)
fun2(5)
fun3(7)