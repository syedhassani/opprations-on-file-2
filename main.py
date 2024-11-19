# # with open("abc.txt","w") as file:
# #  file.write("he saw a duck")

# with open("abc.txt","r") as file:
#     data=file.readlines()
#     for line in data:
#         word=line.split()
#         print(word)

with open("abc.txt") as file:
      data1=file.read()
    
with open("zyz.txt") as file:
     data2=file.read()
data1+="\n"
data1+=data2
with open("new.txt","w") as file:
     file.write(data1)