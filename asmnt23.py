def  fun1(x):
          return x**2
print(fun1(5))



def fun2(num=10):
          if num%2==0:
                    print("number is even")
          else:
                    print("number is odd")
fun2()


def fun3(n=101):
          str_n = str(n)
          l = len(str_n)
          n = int(n)
          rev=0
          tem=int(n)
          for i in range(l):
                    r=n%10
                    rev=rev*10+n
          if rev==tem:
                    print("the number is palindrome")
          else:
                    print("the number is not palindrom")
fun3()


