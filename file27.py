# import re
# pattern="python"
# print(re.findall(pattern,"python is popular language,python ia s future tech,python is easy"))
# # if re.search(pattern,"hello python hai"):
# #           print("matched")
# # else:
# #           print("unmatched")



import re 
pattern="python"
str="hello python am django"
new=re.sub(pattern,"india",str)
print(new)