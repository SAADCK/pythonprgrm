# import re 
# pat="p.th.n"
# if(re.match(pat,"python,a future tech")):
#           print("correct")
          
# else:
#           print("incorrect")



import re
pat="[A-z][0-9][a-z]"
if(re.search(pat,"W7i")):
          print("matched")
          
else:
          print("not matched")