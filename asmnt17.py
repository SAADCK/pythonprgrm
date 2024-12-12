def is_palindrom(number):
          num_str=str(number)
          n=len(num_str)
          for i in range(n // 2):
                    if num_str[i] !=num_str[n - i - 1]:
                              return False
          
          return True
number = int(input("Enter A Number:"))
if is_palindrom(number):
          print(f"{number}is a palindrom.")
else:
          print(f"{number}is not a palindrome.")
